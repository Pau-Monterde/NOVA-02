import os
from engine.models.prompt import Prompt
from huggingface_hub import login
from dotenv import load_dotenv

load_dotenv()

with open(r"C:\Users\paumo\token.txt", "r", encoding="utf-8") as f:
    hf_token = f.readline()
    
login(hf_token)

# Test prompts para evaluar el sistema de extracción de entidades y detección de intenciones.
test_prompts = [

    # ACTION + TARGET
    "Open Spotify",

    # ACTION + TARGET + RECIPIENT
    "Send the photo to John",

    # ACTION + TARGET + LOCATION
    "Find restaurants in Barcelona",

    # ACTION + TARGET + TIME
    "Remind me to call Sarah tomorrow at 5 PM",

    # ACTION + TARGET + RECIPIENT + TIME
    "Send the project report to Michael next Friday",

    # ACTION + TARGET + RECIPIENT + LOCATION + TIME
    "Send the PDF to John in Madrid tomorrow morning",

    # Múltiples recipients
    "Send the report to John and Mary",

    # Múltiples entidades NER
    "Book a meeting with Sarah in London on June 15th",

    # Pregunta natural
    "Can you send the latest project report to Michael through Telegram next Friday at 3 PM?",

    # Voz pasiva (muy útil para probar grammar)
    "John's car needs to be sent to the repair shop tomorrow.",

    # Sin NER
    "Delete the temporary files",

    # Objeto compuesto
    "Create a new Python project",

    # Lugar + persona
    "Meet John at the airport",

    # Fecha relativa
    "Schedule a meeting with Alice next week",

    # Caso complejo
    "Send the presentation to John and Mary via WhatsApp tomorrow at 9 AM from Barcelona"
]

selected_prompt = test_prompts[int(input(os.getenv("ASSISTANT") + ": (0-14) "))]  # Solicitar al usuario que ingrese un prompt para analizar.

print("Analizando el prompt: " + selected_prompt)  # Mostrar el prompt seleccionado para análisis.

prompt = Prompt(selected_prompt)  # Crear una instancia de Prompt con el texto ingresado.

rolesv_list = []

for i in prompt.role_frame.roles:
    rolesv_list.append(f"{i.value}: {i.role}")

# Mostrando el resultado del análisis de entidades, emociones y POS
print(f"""
Resultados del análisis del prompt:

-----------------------------------------------------------
-----------------------------------------------------------
                Analisis Linguístico
-----------------------------------------------------------
      
Entidades POS: {prompt.parsed_text.linguistic_analisys.pos}
Entidades NER: {prompt.parsed_text.linguistic_analisys.ner}
-----------------------------------------------------------
-----------------------------------------------------------
                Extraccion gramatical
-----------------------------------------------------------

Verbo raíz (acción principal): {prompt.parsed_text.grammatical_extraction.root_verb.lemma}

Objeto directo: {prompt.parsed_text.grammatical_extraction.direct_object.lemma}

Objetos indirectos: {prompt.parsed_text.grammatical_extraction.indirect_objects}

-----------------------------------------------------------
-----------------------------------------------------------
                Detección de Roles
-----------------------------------------------------------

Roles detectados: {rolesv_list}

-----------------------------------------------------------
-----------------------------------------------------------
                Detección de Intención
-----------------------------------------------------------

Intención detectada: {prompt.intent.name}
Puntuación: {prompt.intent.score}

-----------------------------------------------------------
-----------------------------------------------------------
                Resultado de la ejecución
-----------------------------------------------------------

Estatus: {prompt.execution}
""")



"""
Input
 ↓
Preprocess
 ↓
Intent Detection
 ↓
Entity Extraction
 ↓
Emotion Analysis
 ↓
Context Check
 ↓
Decision Engine
 ↓
Output
"""
