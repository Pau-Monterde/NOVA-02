import spacy
from engine.models.parser.models import ParsedText
from engine.parser.linguistic.analyzer import linguistic_analisys
from engine.parser.grammar.extractor import grammatical_extraction

nlp = spacy.load("en_core_web_sm")

def parse_text(string):
    doc = nlp(string)

    return ParsedText(linguistic_analisys(doc), grammatical_extraction(doc))