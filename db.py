import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Cargando las variables de entorno (archivo .env)
load_dotenv()

# Inicializando la base de datos
client = MongoClient(os.getenv("MONGO_URL"))
print(os.getenv("ASSISTANT"))
db = client["NOVA-02_DB"]
users = db["users"]
phrases = db["responses"]

