from dotenv import load_dotenv
import openai
import os

load_dotenv()

config = {
    "openai_api_key": os.getenv("OPENAI_API_KEY"),
    "chatgpt_model": os.getenv("CHATGPT_MODEL", "gpt-4o-mini")
}

if not config["openai_api_key"]:
    raise Exception("Missing OPENAI_API_KEY environment variable")

openai.api_key = config["openai_api_key"]

card_options = [
    {
        "name": "El Loco",
        "name_in_context": "del Loco",
        "interpretation": [
            "Este joven busca emprenderse en un viaje. Es un comienzo, sin cargas, por puras ganas e impulso. Lleva consigo solo lo necesario. Viaja liviano y alegre (sus cascabeles). Hay otro personaje presente también: El perro ¿Lo impulsa o lo retiene?",
            "Esta carta nos impulsa a la acción, a animarnos, sin tanta vuelta. En su lado contrario, puede significar que no estemos prestando atención a nuestro alrededor, o que no tengamos en cuenta el afuera."
        ]
    },
    {
        "name": "El Mago",
        "name_in_context": "del Mago",
        "interpretation": [
            "Este aprendiz aparenta estar jugando y probando elementos en su mesa. Hay mucho movimiento pero esta vez es mas de la cabeza, está activando su mente. Esos objetos representan las 4 energias (materia, pulsividad, mente y emoción): por lo tanto, posee el todo en sus manos. Lo que haga con eso, lo puede llevar a donde quiera, solo depende de él.",
            "Eso es en parte el mensaje, jugar, comienzo mental, potencialidad. Pero si ven, también mira al costado, como buscando la aprobación. Esa es una buena observación para hacerse a une misme."
        ]
    },
    {
        "name": "La Sacerdotisa",
        "name_in_context": "de la Sacerdotisa",
        "interpretation": [
            "Se detiene y observa. Está tan tapada que no se sabe qué esconde, pero algo está tramando. Mujer sabia y gestante. Algo va a parir. No necesariamente sea un individuo. Puede ser también un proyecto, una idea.",
            "Es momento de frenarse, de ir hacia dentro.Prepararse para lo que viene. Como una planta que acumula energía para dar a lucir sus hojas. Puede ser una madre o una abuela, que abriga y espera con comida casera."
        ]
    },
    {
        "name": "La Emperatriz",
        "name_in_context": "de la Emperatriz",
        "interpretation": [
            "El famoso KE MUJER! Ella en su trono, cómoda, escudada, activa y mandona. Mujer que puede todo, y hace y deshace a su manera. Madre todopoderosa. Trabaja, materia, proyecta y domina todo a la perfección. Sumamente creativa. Simbólicamente su cetro esta apoyado en su bajo vientre, de donde nace su lado mas creativo.",
            "Aquí ya es momento de dar a conocer eso que proyectamos. De conectarnos con nuestra creatividad. De sabernos poderosos.",
            "Puede que también nos estemos aprovechando de algo, como escalar algo."
        ]
    },
    {
        "name": "El Emperador",
        "name_in_context": "del Emperador",
        "interpretation": [
            "Qué cosas se relacionan con el número 4?… El cuadrado, la casa, la familia tipo. El emperador es todo lo que nos da estabilidad. La comodidad, la seguridad.",
            "Representado por un hombre parado, apoyado con el cetro en su mano y el escudo a sus pies, da la sensación de estar descansando y, a la vez, listo para actuar.",
            "Quizás sea momento de ordenar tus cosas, buscar la estabilidad, de ir a lo seguro. O, por el contrario, estar muy estancado o cómodo, y este es un llamado a ir mas allá de lo conocido."
        ]
    },
    {
        "name": "El Papa",
        "name_in_context": "del Papa",
        "interpretation": [
            "Ya pasamos por las figuras de la corte, los juglares, etc: ahora es momento de ir mas allá, un paso mas, la quinta pata al gato dicen.Sí, es ser rebuscado, porque esta carta trae algo mas allá de lo concreto, trae lo divino, la fé.Pareciese que este personaje da una bendición.",
            "Entonces es momento de salir de la zona de confort. De apostar a algo mas.",
            "Es muy probable que esta carta se relacione a abusos, a engaños o cosas ocultas. Ya que en la parte inferior, pareciesen feligreses de espaldas. Mucho mas pequeños en relación a la figura religiosa, como marcando poder y autoridad por encima de ellos."
        ]
    },
    {
        "name": "Los Enamorados",
        "name_in_context": "de los Enamorados",
        "interpretation": [
            "Primer carta que involucra mas de un personaje. La fascinación del encuentro con otra persona. Y eso hace que traiga confusión.",
            "La persona del medio está, con su cuerpo hacia el personaje de la derecha y con su cabeza al de la izquierda. Da indicio que no sabe qué dirección tomar. Si hacerle caso a su cabeza o a su instinto. Es por eso que aparece cupido. Para flecharlo y que se vuelva a \"enamorar\" de si mismo y aliñe su cabeza de su corazón.",
        ]
    },
    {
        "name": "El Carro",
        "name_in_context": "del Carro",
        "interpretation": [
            "Pongan el carro en movimiento, que los melones, se acomodan solos. Esta frase es en parte la esencia de la carta. Qué debería activar? Me estoy moviendo?",
            "Aqui vemos a un muchacho, en un carro con dos caballos. Pero es un carro adosado; con cortinados y adornos. Él posee una corona y en su armadura, estan las dos caretas del teatro. Identificamos entonces al teatro relacionado con lo bello, lo estético y lo creativo. Así tb puede estar relacionado con no mostrarse tal cual uno es.",
        ]
    },
    {
        "name": "La Justicia",
        "name_in_context": "de la Justicia",
        "interpretation": [
            "Mujer sentada en un trono, posee en una mano una espada, y en la otra, una balanza que no llega a estar equilibrada.",
            "Claro, podría ser una madre mas seria y exigente. Pero esta carta es la primera que nos mira de frente, como si fuésemos espejo, como si nos hablara directo. Esta carta nos esta diciendo justo eso: \"hace cargo\", \"el momento es ahora\", \"no te exijas tanto, no todo es perfecto\". Es una madre que pone limites, pero también lo hace desde el amor.",
        ],
    },
    {
        "name": "El Ermitaño",
        "name_in_context": "del Ermitaño",
        "interpretation": [
            "Me gusta llamarlo \"El manguero del tarot\": y sí, sabe que algo se está por terminar, y como es tan sabio, hace un recorrido recordando los buenos momentos (y tb los malos). Pero le cuesta soltar, sabe que viene otra etapa y es por eso que entra en crisis. Crisis a modo de revisión interna.",
            "Podés soltar? Qué estás revisando?"
        ],
    },
    {
        "name": "La Rueda de la Fortuna",
        "name_in_context": "de la Rueda de la Fortuna",
        "interpretation": [
            "He aquí la carta nro diez.Es una rueda que cierra un ciclo o, que al menos, eso intenta. Porque al ser rueda, puede volver a comenzar. Pero se queda ahí en loop.",
            "Qué debo finalizar? Qué estoy repitiendo?"
        ],
    },
    {
        "name": "La Fuerza",
        "name_in_context": "de la Fuerza",
        "interpretation": [
            "Nos adentramos en un nuevo camino, una nueva búsqueda. Comienza un camino mas profundo.",
            "La mujer está domando al león o el león a ella? La cabeza del animal, pareciese salir de su sexo. Esta imagen nos habla del deseo y del control. Por eso, dejamos la cabeza para conectarnos con nuestra impulsividad, con eso que nos nace.",
            "La pregunta es… Cuál es mi deseo? Estoy controlando? O me dejo controlar?"
        ],
    },
    {
        "name": "El Colgado",
        "name_in_context": "del Colgado",
        "interpretation": [
            "Te detenés a observar, hay algo que te hizo frenar. Algo te hizo ruido pero no le encontrás la vuelta. Ahí es cuando te das vuelta vos y mirás todo de otra manera. Es el famoso  momento \"aha\", en donde te das cuenta que las cosas que pensabas, que te habían dicho, te habían enseñado, etc; no son lo que pensabas. Es un nuevo pensar, un nuevo sentir.",
            "Se cuelga cómodo y tranquilo. Lo sostienen dos pilares, que ven podrían ser arboles. Y de ahí \"pende\" de un cordón. Arbol de familia y cordón umbilical te suenan? Claro, esto puede estar relacionado a cortar con el legado familiar, o con nuestros padres. Pero esto tb aplica para muchas otros momentos adolescentes. Tradiciones, jefes, tiempos, ideas, etc; todos ellos pueden tb romperse, para así transformarse.",
        ],

    },
    {
        "name": "El Arcano sin Nombre",
        "name_in_context": "del Arcano sin Nombre",
        "interpretation": [
            "Es una muerte? Sí. Pero es una transformación y transmutación. Me gusta llamarle momento \"Marie Kondo\". Porque es tiempo de hacer limpieza, de todo tipo: vínculos, trabajos, cosas, acciones, transiciones, ideas, tiempos.",
            "Como ven esta imagen refleja un cuerpo esquelético. Primero se deshace de ru ropaje, hasta quedar en huesos. Pero luego continúa con su hoz arando la tierra, preparando el terreno para la nueva siembra.",
            "Qué debe transformarse en mi vida? Que quiero sembrar? De qué me debo deshacer?"
        ],
    },
    {
        "name": "La Templanza",
        "name_in_context": "de la Templanza",
        "interpretation": [
            "Despues de una tormenta, llega la calma.La templanza se aparece en forma de ángel para alivianar la cosas, para equipararlas, para \"templarlas\"",
            "Esta es una señal, a modo de bendición."
        ]
    },
    {
        "name": "El Diablo",
        "name_in_context": "del Diablo",
        "interpretation": [
            "Este ser alado, andrógino, con tetas, pene, y ojos por todas partes tiene a otros, cual prisioneros, dos a sus pies. En su mano cuenta con una antorcha. Y tb mira de frente, pero algo bizco.",
            "Como su nombre nos indica, es un ángel caído. Que busca la luz, el ascenso. Sabe que primero debe trabajar y ocuparse de su oscuridad.",
            "Esta carta asi como nos enfrenta con nuestros miedos y tentaciones; también nos muestra juegos de poder, abusos , excesos."
        ]
    },
    {
        "name": "La Torre",
        "name_in_context": "de la Torre",
        "interpretation": [
            "La casa Dios, o La torre, muestra una torre coronada, que se abre en su techo y parece destapar algo, y de allí sale algo y explota. Los personajes parecen haber sido expulsados de la misma.",
            "Hay algo que se rompe, se destapa.Es un cambio incómodo, porque nuestra estructura se quiebra.Pero no podemos hacer nada.O nos resistimos y vuelve con fuerza: o lo aceptamos y fluimos.",
            "Se relaciona a cambios estructurales.Ya sea una mudanza, un viaje largo, una separación, la nueva llegada de un integrante, etc.Algo en nuestra vida necesita o está cambiando."
        ]
    },
    {
        "name": "La Estrella",
        "name_in_context": "de la Estrella",
        "interpretation": ["Esta mujer sentada a orillas de un rio, desnuda, volcando dos ánforas, es un símbolo de entrega. Encontró su lugar y su manera de brindarse al mundo. No esconde nada, su entrega es desinteresada y transparente.",
                           "La estrella es esa persona que lo da todo, super generosa, que siempre piensa en los demás.Pero no es una fuente inagotable.Tiene que aprender a que eso que da, tb se lo de a sí misma.",
                           ]
    },
    {
        "name": "La Luna",
        "name_in_context": "de la Luna",
        "interpretation": [
            "Arquetipo de madre por excelencia, esta carta nos muestra dos animales que parecen ser perros/lobos, disputando algo a orillas de un lago, en donde se encuentra un cangrejo que trae una perla. En la tierra se ven dos torres de cada lado de los mamíferos. En el cielo, de noche, una luna sol. Brilla fuerte, e irradia su energía atrapante.",
            "Esta energía profunda nos hace ir a lo seguro, a casa. Tan reconfortante que no puedo salir, es una introspección a la que me es imposible salir, mi cabeza no para, mi imaginación tampoco. El afuera es amenazante.",
            "Por más cómodos que nos sintamos en este espacio, es necesario salir para conectar con la realidad y dejar de hacernos la cabeza."
        ]
    },
    {
        "name": "El Sol",
        "name_in_context": "del Sol",
        "interpretation": [
            "El encuentro con la luz es fuerte, cuesta acostumbrarse. ES adaptación y aceptación pura",
            "Acá vemos como hay dos personajes que aparentan ser iguales. Uno está parado en suelo firme y parece estar ayudando al otro, que se siente mas inseguro. El Sol viene a iluminar eso justamente. El poder aceptar esas dos partes de nosotros, la segura y plantada y la que conlleva miedos y debilidades. Esas dos partes hacen la unidad y nos hacen seres únicos e irrepetibles.",
            "Como arquetipo paterno, esta carta, invita a la acción, a salir, a construir."
        ],
    },
    {
        "name": "El Juicio",
        "name_in_context": "del Juicio",
        "interpretation": [
            "El llamado es claro! Esta trompeta suena a modo de resurrección. Es la bendición! Algo despierta en nosotros, esta alerta suena por algo.",
            "Qué debo despertar en mi ? Cuál es el llamado ?"
        ],
    },
    {
        "name": "El Mundo",
        "name_in_context": "del Mundo",
        "interpretation": [
            "Hemos concluído un ciclo importante. Es una realización. Somos completos, Todos nuestros centros están equilibrados.",
            "Vemos una mujer coronada con cuatro seres alrededor ( un ángel, un águila, un león y un toro). Estas son las cuatro energías: la emocional, la mental, la vital y la material. Así como una coronación de un proceso o de un premio, esto podría representar un encierro, el no poder ver su completitud. También podría ser que el huevo (proyecto) esté listo para salir y así comenzar un nuevo ciclo."
        ],
    }
]

topic_options = {
    "general": {
        "name": "General",
        "question_message": lambda x: f"¿Cómo interpretar {x}?",
    },
    "love": {
        "name": "Amor",
        "question_message": lambda x: f"¿Cómo interpretar {x} con respecto a mis relaciones amorosas?",
    },
    "work": {
        "name": "Trabajo",
        "question_message": lambda x: f"¿Cómo interpretar {x} con respecto a mi trabajo?",
    },
    "money": {
        "name": "Dinero",
        "question_message": lambda x: f"¿Cómo interpretar {x} con respecto a mi dinero?",
    },
    "health": {
        "name": "Salud",
        "question_message": lambda x: f"¿Cómo interpretar {x} con respecto a mi salud?",
    },
    "family": {
        "name": "Familia",
        "question_message": lambda x: f"¿Cómo interpretar {x} con respecto a mi familia?",
    },
    "friendship": {
        "name": "Amistad",
        "question_message": lambda x: f"¿Cómo interpretar {x} con respecto a mis amistades?",
    },
    "spirituality": {
        "name": "Espiritualidad",
        "question_message": lambda x: f"¿Cómo interpretar {x} con respecto a mi espiritualidad?",
    },
    "leisure": {
        "name": "Ocio",
        "question_message": lambda x: f"¿Cómo interpretar {x} con respecto a mi tiempo de ocio?",
    },
    "travel": {
        "name": "Viajes",
        "question_message": lambda x: f"¿Cómo interpretar {x} con respecto a mis viajes?",
    },
    "studies": {
        "name": "Estudios",
        "question_message": lambda x: f"¿Cómo interpretar {x} con respecto a mis estudios?",
    },
    "projects": {
        "name": "Proyectos",
        "question_message": lambda x: f"¿Cómo interpretar {x} con respecto a mis proyectos?",
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


def get_system_prompt(personality_keywords, cards):
    try:
        card_interpretations = []
        for i in cards:
            if i < 0 or i >= len(card_options):
                raise ValueError(f"Invalid card index: {i}")
            card_interpretations.append(card_options[i])

        return '\n'.join([
            "Sos unx tarotista. Da respuestas relativamente concisas y neutrales en cuanto al género.",
            f"Sé {', '.join(map(lambda x: x, personality_keywords[:-1]))} y {personality_keywords[-1]}.",
            f"Sé fiel a los significados tradicionales de las cartas, tomando como referencia lo siguiente:",
            '\n'.join(map(
                lambda x: f"- {x['name']}: {' '.join(x['interpretation'])}", card_interpretations))
        ])
    except Exception as e:
        raise Exception(f"Error generating system prompt: {str(e)}")

# Function to get GPT-4 response


def get_openai_response(personality_keywords, cards, question_message):
    try:
        chatgpt_system = get_system_prompt(personality_keywords, cards)
        response = openai.ChatCompletion.create(
            model=config["chatgpt_model"],
            messages=[
                {"role": "system", "content": chatgpt_system},
                {"role": "user", "content": question_message}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error getting OpenAI response: {str(e)}")


def get_interpretation(cards, topic, question, personality):
    if len(cards) > 1:
        cards_names = f"juntas las cartas {', '.join(map(lambda x: card_options[x]['name_in_context'], cards[:-1]))} y {card_options[cards[-1]]['name_in_context']}"
    else:
        cards_names = f"la carta {card_options[cards[0]]['name_in_context']}"

    if question:
        question_message = f"¿Cómo interpretar {cards_names} en respuesta a esta pregunta? {question}"
    else:
        if not topic:
            topic = "general"
        question_message = topic_options[topic]["question_message"](
            cards_names)

    if not personality:
        personality = "default"
    personality_keywords = personality_options[personality]

    response = get_openai_response(
        personality_keywords, cards, question_message)
    return [question_message, response]
