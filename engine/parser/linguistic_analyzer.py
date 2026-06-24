from engine.models.parser_models import TokenData, EntityData, LinguisticAnalysis
from spacy.tokens.doc import Doc

def linguistic_analisys(doc: Doc):
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