from engine.models.speech_act import SpeechAct
from engine.models.parser_models import ParsedText

def classify_speech_act(parsed_text:ParsedText):
    question_words = ["how", "what", "why", "when", "where", "who"]

    for token in parsed_text.linguistic_analisys.pos:
        if token.lemma in question_words:
            return SpeechAct.QUESTION