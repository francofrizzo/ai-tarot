from dotenv import load_dotenv
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
from urllib import parse
import time
from collections import defaultdict
from typing import Dict, List

from tarot import get_interpretation

# Rate limiting configuration
RATE_LIMIT_REQUESTS = 10  # Maximum requests allowed
RATE_LIMIT_WINDOW = 60  # Time window in seconds
rate_limit_store: Dict[str, List[float]] = defaultdict(list)

def is_rate_limited(ip_address: str) -> bool:
    """
    Check if an IP address has exceeded the rate limit.
    Returns True if rate limited, False otherwise.
    """
    current_time = time.time()
    
    # Remove timestamps older than the window
    rate_limit_store[ip_address] = [
        timestamp for timestamp in rate_limit_store[ip_address]
        if current_time - timestamp < RATE_LIMIT_WINDOW
    ]
    
    # Check if the number of requests in the window exceeds the limit
    if len(rate_limit_store[ip_address]) >= RATE_LIMIT_REQUESTS:
        return True
    
    # Add current timestamp to the store
    rate_limit_store[ip_address].append(current_time)
    return False

load_dotenv()

config = {
    "host": os.getenv("HOST", "0.0.0.0"),
    "port": int(os.getenv("PORT", "3678")),
}

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(CORSRequestHandler, self).end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def get_client_ip(self):
        """Get the client's IP address."""
        return self.client_address[0]

    def do_GET(self):
        # Check rate limit
        client_ip = self.get_client_ip()
        if is_rate_limited(client_ip):
            self.send_response(429)  # Too Many Requests
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "error": "Rate limit exceeded. Please try again later."
            }).encode("utf-8"))
            return

        query = parse.parse_qs(parse.urlsplit(self.path).query)
        cards = query["cards"] if "cards" in query else None
        topic = query["topic"][0] if "topic" in query else None
        question = query["question"][0] if "question" in query else None
        personality = query["personality"][0] if "personality" in query else None


        if not cards:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(bytes("Missing cards parameter", "utf-8"))
            return
  
        cards = [int(card) for card in cards]

        [prompt, response] = get_interpretation(cards, topic, question, personality)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({
            "prompt": prompt,
            "response": response
        }).encode("utf-8"))

print("Listening on {}:{}".format(config["host"], config["port"]))
httpd = HTTPServer((config["host"], config["port"]), CORSRequestHandler)
httpd.serve_forever()
