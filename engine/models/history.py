class ConversationHistory:
    def __init__(self):
        self.entry_list:list[HistoryEntry] = []
    
    def messages_list(self):
        messages_list = []

        for entry in self.entry_list:
            messages_list.append(entry.dict())

        return messages_list

class HistoryEntry:
    def __init__(self, role:str, content:str):
        self.role = role
        self.content = content

    def dict(self):
        return {
            "role": self.role,
            "content": self.content
        }