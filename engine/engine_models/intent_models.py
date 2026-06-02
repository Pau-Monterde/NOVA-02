import re

# Clases Intent i ContextIntent para generar todas las intenciones interpretables
class Intent():
    def __init__(self, name:str, k_words:list[str], r_words:list[str] | None = None):
        self.name = name
        self.k_words = k_words
        self.r_words = r_words

class ContextIntent(Intent):
    def __init__(self, name:str, k_words:list[str]):
        super().__init__(name, k_words)

# Lista de todas las intenciones que el asistente es capaz de interpretar
intent_list = [
    Intent(
        name = "ask_time",
        k_words = ["time", "clock", "hour", "minute", "second", "date", "day", "today", "now", "current"],
        r_words = ["what", "tell"]
    ),

    Intent(
        name = "set_alarm",
        k_words = ["alarm", "wake", "wake up", "ring", "notify"],
        r_words = ["set", "create", "make", "put", "add"]
    ),

    Intent(
        name = "set_reminder",
        k_words = ["remind", "reminder", "remember", "note", "dont forget"],
        r_words = ["set", "create", "add", "make"]
    ),

    Intent(
        name = "play_media",
        k_words = ["play", "music", "song", "track", "audio", "playlist", "sound", "video", "youtube"],
        r_words = ["start", "open", "play"]
    ),

    Intent(
        name = "control_device",
        k_words = ["turn", "switch", "open", "close", "activate", "deactivate", "launch"],
        r_words = ["computer", "spotify", "app", "system", "wifi", "windows"]
    ),

    Intent(
        name = "search_web",
        k_words = ["internet", "online", "google", "chrome"],
        r_words = ["search", "look for", "find", "browse",]
    ),

    Intent(
        name = "small_talk",
        k_words = ["how are you", "hello", "hi", "hey", "what's up", "talk", "chat", "joke"],
    ),

    Intent(
        name = "express_emotion",
        k_words = ["feel", "feeling", "am", "i am", "tired", "sad", "happy", "angry", "stressed", "bored", "excited"]
    ),

    Intent(
        name = "farewell",
        k_words = ["bye", "goodbye", "see you", "later", "exit", "quit", "end"]
    ),

    ContextIntent(
        name = "confirm",
        k_words = ["yes", "yeah", "yep", "correct", "right", "ok", "okay", "sure"]
    ),

    ContextIntent(
        name = "deny",
        k_words = ["no", "nope", "not", "never", "wrong", "false", "don't"]
    ),

    ContextIntent(
        name = "clarify",
        k_words = ["i mean", "actually", "correction", "not that", "change", "instead"]
    )
]

