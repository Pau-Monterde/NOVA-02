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

prompt = Prompt(input(os.getenv("ASSISTANT") + ": "))

try:
    print("Intentión detectada: " + prompt.intent.name)
except:
    pass

print("Entidades detectadas: ")
print(prompt.parsed_text)

print("Resultado del analisis de emociones: ")
print(prompt.emotion)

print("Entidades POS: ")
print(prompt.parsed_text.POS)

print("Entidades NER: ")
print(prompt.parsed_text.NER)

print("Objeto directo: ")
print(prompt.parsed_text.direct_object)

print("Objetos indirectos: ")
print(prompt.parsed_text.indirect_objects)


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
