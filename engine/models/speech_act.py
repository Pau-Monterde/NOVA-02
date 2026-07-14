from enum import Enum

class SpeechAct(Enum):
    EXECUTION = "EXECUTION" # Cuando se pide ejecutar una función
    INFORMATION = "INFORMATION" # Cuando se pide información
    EXPLANATION = "EXPLANATION" # Cuando se pide una explicación
    CONVERSATION = "CONVERSATION" # Cuando se quiere conversar sin un fin
    CONFIRMATION = "CONFIRMATION" # Cuando se quiere confirmar algo
    CLARIFICATION = "CLARIFICATION" # Cuando se esta tratando de aclarar algo
    CORRECTION = "CORRECTION" # Cuando se quiere corregir información erronea del llm
    FEEDBACK = "FEEDBACK" # Para dar nuestro feedback
    UNKNOWN = "UNKNOWN" # Cuando somos incapaces de detectar lo que se quiere

    