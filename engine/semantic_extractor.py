from engine.models.parser_models import ParsedText
from engine.models.semantic_models import RoleType, RoleEntity, RoleFrame
from engine.models.exceptions.context_exceptions import AnyRoleAssignmentException

def deduplicate_roles(roles:list[RoleEntity]):
    seen = []
    seen_values = []

    for role in roles:
        if role.value not in seen_values:
            seen_values.append(role.value)
            seen.append(role)
    return seen

def extract_roles(parsed_text: ParsedText):
    roles:list[RoleEntity] = []

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
        # Extraer roles basados en NER
        if ent.label == "PERSON":
            roles.append(RoleEntity(ent.text, RoleType.RECIPIENT, "NER"))

        elif ent.label in ("GPE", "LOC", "FAC"):
            roles.append(RoleEntity(ent.text, RoleType.LOCATION, "NER"))

        elif ent.label in ("DATE", "TIME"):
            roles.append(RoleEntity(ent.text, RoleType.TIME, "NER"))

        elif ent.label == "ORG":
            roles.append(RoleEntity(ent.text, RoleType.ORGANIZATION, "NER"))

        elif ent.label == "EVENT":
            roles.append(RoleEntity(ent.text, RoleType.EVENT, "NER"))

        elif ent.label in ("PRODUCT", "WORK_OF_ART"):
            roles.append(RoleEntity(ent.text, RoleType.TARGET, "NER"))

        elif ent.label == "LANGUAGE":
            roles.append(RoleEntity(ent.text, RoleType.LANGUAGE, "NER"))

        elif ent.label == "MONEY":
            roles.append(RoleEntity(ent.text, RoleType.MONEY, "NER"))

        elif ent.label == "QUANTITY":
            roles.append(RoleEntity(ent.text, RoleType.QUANTITY, "NER"))

        elif ent.label == "PERCENT":
            roles.append(RoleEntity(ent.text, RoleType.PERCENTAGE, "NER"))

        elif ent.label == "CARDINAL":
            roles.append(RoleEntity(ent.text, RoleType.NUMBER, "NER"))

        elif ent.label == "ORDINAL":
            roles.append(RoleEntity(ent.text, RoleType.ORDINAL, "NER"))

        elif ent.label == "LAW":
            roles.append(RoleEntity(ent.text, RoleType.LAW, "NER"))

        elif ent.label == "NORP":
            roles.append(RoleEntity(ent.text, RoleType.GROUP, "NER"))

    if len(roles) == 0:
        raise AnyRoleAssignmentException()
        
    return RoleFrame(deduplicate_roles(roles))


def roles_extraction(parsed_text:ParsedText):
    semantic_exceptions_list:list[Exception] = []
    try:
        return extract_roles(parsed_text), None
    except AnyRoleAssignmentException as e:
        semantic_exceptions_list.append(e)
        return None, semantic_exceptions_list

    
