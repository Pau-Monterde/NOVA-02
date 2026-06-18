from engine.models.parser.models import ParsedText
from engine.models.semantic.models import RoleType, RoleEntity, RoleFrame

def deduplicate_roles(roles:list[RoleEntity]):
    seen = {}

    for r in roles:
        re = (r.value, r.role)

        if not re in seen:
            seen[re] = r

    return list(seen.values())

def extract_roles(parsed_text: ParsedText):
    roles = []

    grammar = parsed_text.grammatical_extraction
    ner = parsed_text.linguistic_analisys.ner

    # Extraer roles basados en la gramática con clases de rol
    
    if grammar.root_verb:
        roles.append(RoleEntity(grammar.root_verb.lemma, RoleType.ACTION, "GRAMMAR"))
    
    if grammar.direct_object:
        roles.append(RoleEntity(grammar.direct_object.lemma, RoleType.TARGET, "GRAMMAR"))

    if len(grammar.indirect_objects) > 0:
        for obj in grammar.indirect_objects:
            roles.append(RoleEntity(obj.lemma, RoleType.RECIPIENT, "GRAMMMAR"))
    
    # Extraer roles basados en NER
    for ent in ner:
        if ent.label == "PERSON":
            roles.append(RoleEntity(ent.text, RoleType.RECIPIENT, "NER"))

        if ent.label == ("GPE", "LOC"):
            roles.append(RoleEntity(ent.text, RoleType.LOCATION, "NER"))

        if ent.label == ("DATE", "TIME"):
            roles.append(RoleEntity(ent.text, RoleType.TIME, "NER"))
    
    return RoleFrame(deduplicate_roles(roles))


    
