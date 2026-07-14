from pymongo import MongoClient
from engine.models.history import ConversationHistory, HistoryEntry

client = MongoClient("mongodb://localhost:27017/")
db = client["NOVA-02-DB"]
conversations = db["conversations-history"]

def save_conversation(conversation_history: ConversationHistory):
    conversations.insert_one({f"conversation {conversations.count_documents({})}": conversation_history.dict_list()})
