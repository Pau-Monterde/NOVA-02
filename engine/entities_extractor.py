from annotated_types import doc
import spacy
from collections import defaultdict
from spacy.tokens.doc import Doc
from engine.engine_models.text_parser.parsed_text import TokenData, EntityData, LinguisticAnalysis, GramaticalExtraction, ParsedText

nlp = spacy.load("en_core_web_sm")

def linguistic_analysis(doc: Doc):
    # POS
    tokens:list[TokenData] = []
    
    for token in doc:
        if not token.is_punct and not token.is_stop:
            tokens.append(TokenData(token.text, token.lemma_, token.dep_, token.head.text))
            
    
    # NER
    ner_list:list[EntityData] = []

    for ent in doc.ents:
        ner_list.append(EntityData(ent.text, ent.label_, ent.start_char, ent.end_char))
    
    return LinguisticAnalysis(tokens, ner_list)

# Función para extraer la acción principal del prompt, que se corresponde con el verbo raíz (ROOT) de la frase.
def extract_action(doc: Doc):
    for token in doc:
        if token.dep_ == "ROOT" and token.pos_ == "VERB":
            return TokenData(token.text, token.lemma_, token.dep_, token.head.text)
    return None

# Función para extraer el objeto directo del prompt, que se corresponde con el token que tiene una dependencia de "dobj" o "obj".
def extract_direct_object(doc: Doc):
    for token in doc:
        if token.dep_ in ("dobj", "obj", "attr", "oprd"):
            return TokenData(token.text, token.lemma_, token.dep_, token.head.text)
    return None

def extract_indirect_objects(doc: Doc):
    objs:list[TokenData] = []

    for token in doc:
        if token.dep_ in ("pobj", "dative"):
            objs.append(TokenData(token.text, token.lemma_, token.dep_, token.head.text))
    return objs

def grammatical_extraction(doc: Doc):

    # Verbo raíz del prompt
    root_verb = extract_action(doc)

    # Objeto directo del prompt
    direct_object = extract_direct_object(doc)

    # Objetos indirectos del prompt
    indirect_objects = extract_indirect_objects(doc)

    return GramaticalExtraction(root_verb, direct_object, indirect_objects)

def parse_text(string):
    doc = nlp(string)

    return ParsedText(linguistic_analysis(doc), grammatical_extraction(doc))