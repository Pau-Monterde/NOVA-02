from engine.models.parser.models import ParsedText
from engine.models.semantic.models import SlotData, SemanticExtraction

PERSON_NER = "PERSON"
LOCATION_NER = "GPE"

def extract_semantic(parsed_text: ParsedText) -> SemanticExtraction:
    slots = SlotData()
    
    if parsed_text.grammatical_extraction.root_verb:
        slots.action = parsed_text.grammatical_extraction.root_verb.lemma_
    
    if parsed_text.grammatical_extraction.direct_object:
        slots.object = parsed_text.grammatical_extraction.direct_object.lemma_
    
    if parsed_text.grammatical_extraction.indirect_objects:
        for ent in parsed_text.linguistic_analisys.ner:
            if ent.label == "PERSON":
                slots.person = ent
            elif ent.label == "GPE":
                slots.location = ent
    
    return SemanticExtraction(slots)

    
