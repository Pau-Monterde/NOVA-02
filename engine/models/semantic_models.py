from enum import Enum

class RoleType(Enum):
    ACTION = "ACTION"
    TARGET = "TARGET"
    RECIPIENT = "RECIPIENT"
    LOCATION = "LOCATION"
    TIME = "TIME"
    ORGANIZATION = "ORGANIZATION"
    EVENT = "EVENT"
    LANGUAGE = "LANGUAGE"
    MONEY = "MONEY"
    QUANTITY = "QUANTITY"
    PERCENTAGE = "PERCENTAGE"
    NUMBER = "NUMBER"
    ORDINAL = "ORDINAL"
    LAW = "LAW"
    GROUP = "GROUP"

class RoleEntity():
    def __init__(self, value:str, role:RoleType, source:str):
        self.value = value
        self.role = role
        self.source = source

class RoleFrame:
    def __init__(self, roles:list[RoleEntity]):
        self.roles = roles

    def get_role(self, s_role):
        for role in self.roles:
            if role.role.value == s_role:
                return role
    
    def get_roles(self):
        return self.roles
    
    def show_roles(self):
        for role in self.roles:
            print(role.value + " - " + role.role.value + " - " + role.source)

class SemanticExceptions():
    def __init__(self, semantic_exceptions:list[Exception]):
        self.semantic_exceptions = semantic_exceptions