from pymongo import MongoClient
from pymongo.results import InsertOneResult
from engine.models.history import ConversationHistory, HistoryEntry
from engine.models.user_model import UserData
from engine.models.exceptions.db_exceptions import UserNotFound

client = MongoClient("mongodb://localhost:27017/")
db = client["NOVA-02-DB"]
conversations = db["conversations-history"]
user = db["user"]

def save_conversation(conversation_history: ConversationHistory):
    result:InsertOneResult = conversations.insert_one({f"conversation {conversations.count_documents({})}": conversation_history.messages_list()})
    return result

def actualize_conversation(result:InsertOneResult, saved_conversation:ConversationHistory):
    conversations.find_one_and_replace({"_id": result.inserted_id}, {f"conversation {conversations.count_documents({})}": saved_conversation.messages_list()})

def save_user(user_data:UserData):
    user.insert_one(dict(user_data))

def get_user():
    try:
        ud_dict = user.find_one()
        if not ud_dict: raise UserNotFound()
        return UserData.model_validate(ud_dict)
    except:
        new_user = UserData.Create_User()
        save_user(new_user)
        return new_user