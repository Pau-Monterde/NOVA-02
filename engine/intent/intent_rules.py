from engine.models.intent_models import IntentRule, ContextIntent
from engine.executor.skills.file_sender import send_file
from engine.executor.skills.app_opening import open_app
from engine.executor.skills.clock import show_current_time
from engine.executor.skills.spotify_control import spotify_control, next_track, prev_track, play, pause
from engine.executor.skills.get_weather import show_wheather

EXECUTION_RULES = [
    IntentRule(
        name = "SPOTIFY_CONTROL",
        actions = ["play", "open", "run", "put", "reproduce"],
        required_roles = ["TARGET"],
        keywords = ["spotify", "music"],
        context_intents = [
            ContextIntent(
                name = "PLAY",
                actions = ["start", "play"],
                min_score = 30,
                execution = play
            ),

            ContextIntent(
                name = "PAUSE",
                actions = ["stop", "pause"],
                min_score = 30,
                execution = pause
            ),

            ContextIntent(
                name = "NEXT_SONG",
                actions = ["pass", "next"],
                min_score = 30,
                execution = next_track
            ),

            ContextIntent(
                name = "PREV_SONG",
                actions = ["last", "previous"],
                min_score = 30,
                execution = prev_track
            ),
        ],
        execution = spotify_control
    ),

    IntentRule(
        name = "SET_ALARM",
        actions = ["set", "put", "create"],
        keywords = ["alarm"],
        execution = None
    ),

    IntentRule(
        name = "OPEN_APP",
        actions = ["open"],
        required_roles = ["TARGET"],
        keywords = ["spotify", "chrome", "whatsapp"],
        execution = open_app
    ),

    IntentRule(
        name = "SEND_FILE",
        actions = ["send"],
        required_roles = ["TARGET", "RECIPIENT"],
        keywords = ["file", "document", "attachment"],
        execution = send_file
    )
]

INFORMATION_RULES = [
    IntentRule(
        name = "SHOW_CURRENT_TIME",
        actions = ["show", "tell", "display", "what"],
        required_roles = [],
        keywords = ["time", "clock", "hour"],
        execution = show_current_time
    ),

    IntentRule(
        name = "SHOW_WEATHER",
        actions = ["show", "tell", "display", "what", "how"],
        keywords = ["weather", "temperature"],
        execution = show_wheather
    ),
]

EXPLANATION_RULES = [
    IntentRule(
        name = "EXPLAIN_CONCEPT",
        actions = ["how", "why", "explain", "describe", "tell"],
        required_roles = [],
        keywords = ["about"],
        execution = None
    )
]  

CONVERSATION_RULES = [
    IntentRule(
        name = "SMALL_CONVERSATION",
        actions = ["are"],
        required_roles = [],
        keywords = ["hi", "hello", "hey", "morning", "how"],
        execution = None
    )
]

CONFIRMATION_RULES = []

CLARIFICATION_RULES = []

CORRECTION_RULES = []

FEEDBACK_RULES = []

UNKNOWN_RULES = []


