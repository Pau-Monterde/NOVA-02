from engine.engine_models.intent_models import Intent, intent_list
from engine.engine_models.exceptions.IntentNotFound import IntentNotFoundException

def calculate_intents_confidency(w_list:list):
    intent_posibilities:dict = {}

    # Por cada palabra del prompt que coincida con una lista de las palabras de intent sumara su cantidad correpondiente de confianza 
    for intent in intent_list:
        confidence_score = 0
        
        for k_word in intent.k_words:
            if k_word in w_list:
                confidence_score += 1
            
            if intent.r_words:
                for r_word in intent.r_words:
                    if r_word in w_list:
                        confidence_score += 0.5

        # Si la confianza en el intent és mayor a 0, se añade a un dict de intents posibles    
        if confidence_score > 0:
            intent_posibilities[intent] = confidence_score
    
    return intent_posibilities

def select_intent(intent_posibilities:dict):
    best_intent = None
    best_intent_cscore = 0

    # Por cada intent posible del diccionario, si la confianza és mayor al best_intent_cscore, este pasa a ser el escojido (best_intent). 
    # Si la confianza en un intent és igual a best_intent_cscore, significa que se repite la confianza, y que no se puede escoger un intent (IntentNotFoundException)
    for p_intent, c_score in intent_posibilities.items():
        if c_score > best_intent_cscore:
            best_intent = p_intent
            best_intent_cscore = c_score
        
        elif c_score == best_intent_cscore:
            best_intent = None
            raise IntentNotFoundException()
    return best_intent

def select_intent_manually(intent_posibilities:dict[Intent, int]):
    intent_posibilities_list = []

    for p_intent in intent_posibilities.keys():
        intent_posibilities_list.append(p_intent)
    
    if len(intent_posibilities_list) == 0:
        raise IntentNotFoundException

    for i in range(len(intent_posibilities_list)):
        print(str(i) + " --> " + intent_posibilities_list[i].name)

    selected_intent = int(input("Sorry, I couldn't detect correctly your intent with this prompt, what did you want me to do? (Introduce number): "))
    return intent_posibilities_list[selected_intent]

# Funcion para detectar la intención del prompt
def detect_intent(w_list:list):
    intent_posibilities = calculate_intents_confidency(w_list)
    try:
        intent = select_intent(intent_posibilities)
    except IntentNotFoundException as e:
        try: 
            intent = select_intent_manually(intent_posibilities)
        except IntentNotFoundException as e:
            return
            
    return intent


           
    