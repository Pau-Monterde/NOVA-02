from collections import defaultdict

# Capa linguística

class TokenData:
    def __init__(self, text:str, lemma:str, dep:str, head_text:str):
        self.text = text
        self.lemma = lemma
        self.dep = dep
        self.head_text = head_text

class EntityData:
    def __init__(self, text:str, label:str, start:int, end:int):
        self.text = text
        self.label = label
        self.start = start
        self.end = end

class LinguisticAnalysis():
    def __init__(self, pos: list[TokenData], ner: list[EntityData]):
        self.pos = pos
        self.ner = ner

# Capa gramatical

class GrammaticalExtraction():
    def __init__(self, root_verb:TokenData, direct_object:TokenData, indirect_objects:list[TokenData]):
        self.root_verb = root_verb
        self.direct_object = direct_object
        self.indirect_objects = indirect_objects

class ParsedText():
    def __init__(self, linguistic_analisys:LinguisticAnalysis, grammatical_extraction:GrammaticalExtraction):
        self.linguistic_analisys = linguistic_analisys
        self.grammatical_extraction = grammatical_extraction

