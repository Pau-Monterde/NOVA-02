import spacy
from collections import defaultdict
from spacy.tokens.doc import Doc
from engine.engine_models.extracted_entities import ParsedText

nlp = spacy.load("en_core_web_sm")

# Función para extraer la acción principal del prompt, que se corresponde con el verbo raíz (ROOT) de la frase.
def extract_action(doc: Doc):
    for token in doc:
        if token.dep_ == "ROOT" and token.pos_ == "VERB":
            return {
                "text": token.text,
                "lemma": token.lemma_,
                "dep": token.dep_,
                "head": token.head.text
                }
    return None

# Función para extraer el objeto directo del prompt, que se corresponde con el token que tiene una dependencia de "dobj" o "obj".
def extract_direct_object(doc: Doc):
    for token in doc:
        if token.dep_ in ("dobj", "obj", "attr", "oprd"):
            return {
                "text": token.text,
                "lemma": token.lemma_,
                "dep": token.dep_,
                "head": token.head.text
                }
    return None

def extract_indirect_objects(doc: Doc):
    objs = []

    for token in doc:
        if token.dep_ in ("pobj", "dative"):
            objs.append({
                "text": token.text,
                "lemma": token.lemma_,
                "dep": token.dep_,
                "head": token.head.text
                })
    return objs

def parse_text(string):
    doc = nlp(string)

    # POS
    pos_dfdict = defaultdict(list)
    
    for token in doc:
        if not token.is_punct and not token.is_stop:
            pos_dfdict[token.pos_].append({
                "text": token.text,
                "lemma": token.lemma_,
                "dep": token.dep_,
                "head": token.head.text
                })
            print(token.text + ": " + token.dep_)
    
    # NER
    ner_dfdict = defaultdict(list)

    for ent in doc.ents:
        if not ner_dfdict[ent.label_]:
            ner_dfdict[ent.label_].append({
                "text": ent.text,
                "start": ent.start_char,
                "end": ent.end_char,
            })
    
    # Verbo raíz del prompt
    root_verb = extract_action(doc)

    # Objeto directo del prompt
    direct_object = extract_direct_object(doc)

    # Objetos indirectos del prompt
    indirect_objects = extract_indirect_objects(doc)

    return ParsedText(dict(pos_dfdict), dict(ner_dfdict), root_verb, direct_object, indirect_objects)