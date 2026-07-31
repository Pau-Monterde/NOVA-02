from pymongo import MongoClient
from pymongo.results import InsertOneResult
from engine.models.history import ConversationHistory, HistoryEntry

client = MongoClient("mongodb://localhost:27017/")
db = client["NOVA-02-DB"]
conversations = db["conversations-history"]

def save_conversation(conversation_history: ConversationHistory):
    result:InsertOneResult = conversations.insert_one({f"conversation {conversations.count_documents({})}": conversation_history.messages_list()})
    return result

def actualize_conversation(result:InsertOneResult, saved_conversation:ConversationHistory):
    conversations.find_one_and_replace({"_id": result.inserted_id}, {f"conversation {conversations.count_documents({})}": saved_conversation.messages_list()})