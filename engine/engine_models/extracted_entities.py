from collections import defaultdict

class ParsedText():
    def __init__(self, POS:defaultdict[str,str], NER:defaultdict[str,str], root_verb:str, direct_object:str, indirect_objects:list[str]):
        self.POS = POS
        self.NER = NER
        self.root_verb = root_verb
        self.direct_object = direct_object
        self.indirect_objects = indirect_objects