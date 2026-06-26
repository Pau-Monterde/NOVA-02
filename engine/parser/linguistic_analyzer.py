from engine.models.parser_models import TokenData, EntityData, LinguisticAnalysis
from engine.models.exceptions.context_exceptions import POSNotFoundInDocException, NERNotFoundInDocException
from spacy.tokens.doc import Doc

def POS_extraction(doc: Doc, tokens:list[TokenData]):
    for token in doc:
            tokens.append(TokenData(token.text, token.lemma_, token.dep_, token.head.text))

    if len(tokens) == 0:
        raise POSNotFoundInDocException()
    
    return tokens

def NER_extraction(doc: Doc, ner_list:list[EntityData]):
    for ent in doc.ents:
        ner_list.append(EntityData(ent.text, ent.label_, ent.start_char, ent.end_char))
    
    if len(ner_list) == 0:
        raise NERNotFoundInDocException()
    
    return ner_list
    

def linguistic_analisys(doc: Doc):
    analyzer_exceptions:list[Exception] = []

    # POS
    tokens:list[TokenData] = []
    ner_list:list[EntityData] = []
    try: 
        tokens = POS_extraction(doc, tokens)

        # NER
        try:
            ner_list = NER_extraction(doc, ner_list)

        except NERNotFoundInDocException as e:
            analyzer_exceptions.append(e)

    except POSNotFoundInDocException as e:
        analyzer_exceptions.append(e)  
    
    return LinguisticAnalysis(tokens, ner_list), analyzer_exceptions