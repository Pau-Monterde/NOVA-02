from engine.executor.skills.file_sender import send_file
from engine.executor.skills.app_opening import open_app
from engine.executor.skills.clock import show_current_time
from engine.intent.evaluator import score_rule
from engine.models.intent_models import Intent, IntentRule

EXECUTION_RULES = [
    IntentRule(
        name="OPEN_APP",
        actions=["open"],
        required_roles=["TARGET"],
        keywords=["spotify", "chrome", "whatsapp"],
        execution = open_app
    ),

    IntentRule(
        name="SEND_FILE",
        actions=["send"],
        required_roles=["TARGET", "RECIPIENT"],
        keywords=["file", "document", "attachment"],
        execution = send_file
    )
]

INFORMATION_RULES = [
    IntentRule(
        name="SHOW_CURRENT_TIME",
        actions=["show", "tell", "display", "what"],
        required_roles=[],
        keywords=["time", "clock", "hour"],
        execution = show_current_time
    )
]

EXPLANATION_RULES = [
    IntentRule(
        name="EXPLAIN_CONCEPT",
        actions=["how", "why", "explain", "describe", "tell"],
        required_roles=[],
        keywords=["about"],
        execution=None
    )
]  

CONVERSATION_RULES = [
    IntentRule(
        name="SMALL_CONVERSATION",
        actions=["are"],
        required_roles = [],
        keywords=["hi", "hello", "hey", "morning", "how"],
        execution=None
    )
]

CONFIRMATION_RULES = []

CLARIFICATION_RULES = []

CORRECTION_RULES = []

FEEDBACK_RULES = []

UNKNOWN_RULES = []


