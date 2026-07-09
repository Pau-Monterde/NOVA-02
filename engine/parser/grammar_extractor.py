from engine.models.parser_models import TokenData, GrammaticalExtraction
from engine.models.exceptions.context_exceptions import NotRootVerbInContextException, NotDirectObjInContextException, NotIndObjsInContextException
from spacy.tokens.doc import Doc
from spacy.tokens.token import Token

def score_rv_candidate(token:Token):
    score = 0

    if token.dep_ == "ROOT":
        score += 50

    if token.pos_ == "VERB":
        score += 40
    elif token.pos_ == "AUX":
        score += 20

    for child in token.children:
        if child.dep_ in ("obj", "dobj", "pobj"):
            score += 30
    
    if token.lemma_ in ("do", "have", "be"):
        score -= 20
    
    return score

# Función para extraer la acción principal del prompt, que se corresponde con el verbo raíz (ROOT) de la frase.
def extract_root_verb(doc: Doc):
    rv_best_candidate:Token | None = None
    best_token_score = 0

    for token in doc:
        token_score = score_rv_candidate(token)
        
        if token_score > best_token_score:
            best_token_score = token_score
            rv_best_candidate = token
        
    if not rv_best_candidate:
        raise NotRootVerbInContextException()
        
    return TokenData(rv_best_candidate.text, rv_best_candidate.lemma_, rv_best_candidate.dep_, rv_best_candidate.head.text)
    
# Función para extraer el objeto directo del prompt, que se corresponde con el token que tiene una dependencia de "dobj" o "obj".
def extract_direct_object(doc: Doc):
    for token in doc:
        if token.head.dep_ == "ROOT" and token.pos_ in ("NOUN", "PROPN"):
            return TokenData(token.text, token.lemma_, token.dep_, token.head.text)
    
    raise NotDirectObjInContextException()

def extract_indirect_objects(doc: Doc):
    objs:list[TokenData] = []

    for token in doc:
        if token.dep_ in ("pobj", "dative"):
            objs.append(TokenData(token.text, token.lemma_, token.dep_, token.head.text))
    return objs

def grammatical_extraction(doc: Doc):
    extractor_exceptions:list[Exception] = []

    try: 
        # Verbo raíz del prompt
        root_verb = extract_root_verb(doc)
    except NotRootVerbInContextException as e:
        extractor_exceptions.append(e)
        root_verb = None

    try: 
        # Objeto directo del prompt
        direct_object = extract_direct_object(doc)
    except NotDirectObjInContextException as e:
        extractor_exceptions.append(e)
        direct_object = None

    try:
        # Objetos indirectos del prompt
        indirect_objects = extract_indirect_objects(doc)
    except NotIndObjsInContextException as e:
        extractor_exceptions.append(e)
        indirect_objects = None

    return GrammaticalExtraction(root_verb, direct_object, indirect_objects), extractor_exceptions