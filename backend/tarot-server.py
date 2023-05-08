from dotenv import load_dotenv
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
from urllib import parse

from tarot import get_interpretation

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

    def do_GET(self):
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
