import os
from engine.engine_models.prompt import Prompt
from engine.intent_manager import detect_intent 
import spacy, chunk, token
from huggingface_hub import login
from dotenv import load_dotenv

load_dotenv()

with open(r"C:\Users\paumo\token.txt", "r", encoding="utf-8") as f:
    hf_token = f.readline()
    
login(hf_token)

# Test prompts para evaluar el sistema de extracción de entidades y detección de intenciones.
test_prompts = [
    "Send the photo",

    "Send the photo to John",

    "Remind me to call Sarah tomorrow at 5 PM",

    "Send the PDF to John and Mary via WhatsApp tomorrow morning",

    "Can you send the latest project report to Michael through Telegram next Friday at 3 PM?",

    # Bonus (más complejo)
    "John's car needs to be sent to the repair shop tomorrow."
]

selected_prompt = test_prompts[int(input(os.getenv("ASSISTANT") + ": (0-5) "))]  # Solicitar al usuario que ingrese un prompt para analizar.

print("Analizando el prompt: " + selected_prompt)  # Mostrar el prompt seleccionado para análisis.

prompt = Prompt(selected_prompt)  # Crear una instancia de Prompt con el texto ingresado.

# Mostrando el resultado del análisis de entidades, emociones y POS
print(f"""
Resultados del análisis del prompt:

-----------------------------------------------------------
-----------------------------------------------------------
                Analisis Linguístico
-----------------------------------------------------------
      
Entidades POS: {prompt.parsed_text.POS}
Entidades NER: {prompt.parsed_text.NER}
-----------------------------------------------------------
-----------------------------------------------------------
                Extraccion gramatical
-----------------------------------------------------------

Verbo raíz (acción principal): {prompt.parsed_text.root_verb}

Objeto directo: {prompt.parsed_text.direct_object}

Objetos indirectos: {prompt.parsed_text.indirect_objects}

-----------------------------------------------------------
-----------------------------------------------------------
                Detección de Intenciones
-----------------------------------------------------------

                Aun no implementada

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


Hi, today is a cold day. I would like to prove your capacity to talk and detect intents while your engine, designed by my separe all the entities of these text using spacy. Can you tell me the current time, please?
"""
