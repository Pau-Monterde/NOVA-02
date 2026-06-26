# Capa semántica

class RoleType():
    ACTION = "ACTION"
    AGENT = "AGENT"
    TARGET = "TARGET"
    RECIPIENT = "RECIPIENT"
    LOCATION = "LOCATION"
    TIME = "TIME"

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
            if role.role == s_role:
                return role
    
    def show_roles(self):
        for role in self.roles:
            print(role)