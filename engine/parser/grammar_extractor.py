from engine.models.parser_models import TokenData, EntityData, GrammaticalExtraction
from engine.models.exceptions.context_exceptions import NotActionInContextException, NotDirectObjInContextException, NotIndObjsInContextException
from spacy.tokens.doc import Doc

# Función para extraer la acción principal del prompt, que se corresponde con el verbo raíz (ROOT) de la frase.
def extract_root_verb(doc: Doc):
    for token in doc:
        if token.dep_ == "ROOT" and token.pos_ == "VERB":
            return TokenData(token.text, token.lemma_, token.dep_, token.head.text)
        
    for token in doc:
        if token.pos_ == "VERB":
            return TokenData(token.text, token.lemma_, token.dep_, token.head.text)
    
    for token in doc:
        if not token.is_stop and token.is_alpha:
            return TokenData(token.text, token.lemma_, token.dep_, token.head.text)
    
    raise NotActionInContextException()


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
    extractor_exceptions = []

    try: 
        # Verbo raíz del prompt
        root_verb = extract_root_verb(doc)
    except NotActionInContextException as e:
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
    except NotIndObjsInContextException:
        extractor_exceptions.append(e)
        indirect_objects = None

    return GrammaticalExtraction(root_verb, direct_object, indirect_objects), extractor_exceptions