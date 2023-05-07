import openai

openai_api_key = ""
chatgpt_model = "gpt-3.5-turbo"

openai.api_key = openai_api_key

card_options = [
    "del Loco",
    "del Mago",
    "de la Sacerdotisa",
    "de la Emperatriz",
    "del Emperador",
    "del Papa",
    "de los Enamorados",
    "del Carro",
    "La Justicia",
    "del Ermitaño",
    "La Rueda de la Fortuna",
    "La Fuerza",
    "del Colgado",
    "del Arcano sin Nombre",
    "de la Templanza",
    "del Diablo",
    "de la Torre",
    "de la Estrella",
    "de la Luna",
    "del Sol",
    "del Juicio",
    "del Mundo",
]

topic_options = {
    "general": {
        "name": "General",
        "prompt": lambda x: f"¿Cómo interpretar {x}?",
    },
    "love":{
        "name": "Amor",
        "prompt": lambda x: f"¿Cómo interpretar {x} con respecto a mis relaciones amorosas?",
    },
    "work": {
        "name": "Trabajo",
        "prompt": lambda x: f"¿Cómo interpretar {x} con respecto a mi trabajo?",
    },
    "money": {
        "name": "Dinero",
        "prompt": lambda x: f"¿Cómo interpretar {x} con respecto a mi dinero?",
    },
    "health": {
        "name": "Salud",
        "prompt": lambda x: f"¿Cómo interpretar {x} con respecto a mi salud?",
    },
    "family": {
        "name": "Familia",
        "prompt": lambda x: f"¿Cómo interpretar {x} con respecto a mi familia?",
    },
    "friendship": {
        "name": "Amistad",
        "prompt": lambda x: f"¿Cómo interpretar {x} con respecto a mis amistades?",
    },
    "spirituality": {
        "name": "Espiritualidad",
        "prompt": lambda x: f"¿Cómo interpretar {x} con respecto a mi espiritualidad?",
    },
    "leisure": {
        "name": "Ocio",
        "prompt": lambda x: f"¿Cómo interpretar {x} con respecto a mi tiempo de ocio?",
    },
    "travel": {
        "name": "Viajes",
        "prompt": lambda x: f"¿Cómo interpretar {x} con respecto a mis viajes?",
    },
    "studies": {
        "name": "Estudios",
        "prompt": lambda x: f"¿Cómo interpretar {x} con respecto a mis estudios?",
    },
    "projects": {
        "name": "Proyectos",
        "prompt": lambda x: f"¿Cómo interpretar {x} con respecto a mis proyectos?",
    }
}

personality_options = {
    "default": ["serious", "analytical", "thoughtful"],
    "sarcastic": ["ironic", "acid", "teasing"],
    "creative": ["creative", "imaginative", "inspired"],
    "practical": ["practical", "down-to-earth", "realistic", "no-nonsense"],
    "esoteric": ["esoteric", "mystical", "intuitive", "spiritual"],
    "optimistic": ["optimistic", "hopeful", "cheerful"],
    "pessimistic": ["pessimistic", "negative", "gloomy"],
}

# Function to get GPT-4 response
def get_gpt4_response(personality_keywords, prompt):
    chatgpt_system = f"You are a tarotist. Be true to the the traditional meanings of the cards. Give relatively concise, gender-neutral answers. Be {', '.join(map(lambda x: x, personality_keywords[:-1])) } and {personality_keywords[-1]}."
    response = openai.ChatCompletion.create(
        model=chatgpt_model,
        messages=[
            {"role": "system", "content": chatgpt_system},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def get_interpretation(cards, topic, question, personality):
    if len(cards) > 1:
        cards_names = f"juntas las cartas {', '.join(map(lambda x: card_options[x], cards[:-1]))} y {card_options[cards[-1]]}"
    else:
        cards_names = f"la carta {card_options[cards[0]]}"

    if question:
        prompt = f"¿Cómo interpretar {cards_names} en respuesta a esta pregunta? {question}"
    else:
        if not topic:
            topic = "general"
        prompt = topic_options[topic]["prompt"](cards_names)

    if not personality:
        personality = "default"
    personality_keywords = personality_options[personality]

    response = get_gpt4_response(personality_keywords, prompt)
    return [prompt, response]
