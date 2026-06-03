class AccesibleApp():
    def __init__(self, name:str, executable_path:str):
        self.name = name,
        self.executable_path = executable_path

ACCESIBLE_APP_DEFAULT_LIST = [
    AccesibleApp("whatsapp", "/whatsapp.exe"),
    AccesibleApp("telegram", "/telegram.exe"),
    AccesibleApp("discord", "/discord.exe"),
    AccesibleApp("gmail", "/gmail.exe"),
    AccesibleApp("spotify", "/spotify.exe"),
]
