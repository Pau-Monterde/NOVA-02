import spacy
from engine.models.parser_models import ParsedText
from engine.models.parser_models import LinguisticAnalysis, GrammaticalExtraction, ParserExceptions
from engine.models.exceptions.context_exceptions import LinguisticAnalyzerFatalException, POSNotFoundInDocException, NERNotFoundInDocException
from engine.parser.linguistic_analyzer import linguistic_analisys
from engine.parser.grammar_extractor import grammatical_extraction

nlp = spacy.load("en_core_web_sm")

def parse_text(string):
    doc = nlp(string)
    analisys, analyzer_exceptions = linguistic_analisys(doc)
    for i in range(len(analyzer_exceptions)):
        if type(analyzer_exceptions[i]) == POSNotFoundInDocException:
            raise LinguisticAnalyzerFatalException(analyzer_exceptions[i]) 
                
    extraction, extractor_exceptions = grammatical_extraction(doc)
    # for i in range(len(extractor_exceptions)):
    #     if type(extractor_exceptions[i]) == Exception:
    #         raise Exception(analyzer_exceptions[i]) 

    return ParsedText(analisys, extraction), ParserExceptions(analyzer_exceptions, extractor_exceptions)  