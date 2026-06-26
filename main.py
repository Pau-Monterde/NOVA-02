import os
from engine.models.exceptions.context_exceptions import ContextNotCreatedException
from engine.context_generator import generate_rcontext
from engine.models.context_model import RequestContext
from engine.executor.executor import execute

def context_generation(prompt:str):
    print("Analizando el prompt: " + prompt)  # Mostrar el prompt seleccionado para análisis.

    context:RequestContext = generate_rcontext(prompt)  # Crear una instancia de Prompt con el texto ingresado.

    if not context.status.success:
        raise ContextNotCreatedException() 
    
    return context
    
def chatbot(prompt:str):

    try:
        context:RequestContext = context_generation(prompt)
    

        print("------------------------------------------ LINGUISTIC ANALISYS ------------------------------------------")

        print("--------------------- IMPORTANT POS ---------------------")
        for token in context.parsed_text.linguistic_analisys.pos:
            print(token.text + ": " + token.dep)

        print("--------------------- NER ---------------------")
        for ent in context.parsed_text.linguistic_analisys.ner:
            print(ent.text + ": " + ent.label)

        # print("------------------------------------------ GRAMATICAL EXTRACTION ------------------------------------------")

        # print("Root verb: " + context.parsed_text.grammatical_extraction.root_verb.text)

        # print("Direct object: " + context.parsed_text.grammatical_extraction.direct_object.text)

        # for in_obj in context.parsed_text.grammatical_extraction.indirect_objects:
        #     print("Object: " + in_obj.text)
        #     print("Object parent: " + in_obj.head_text)

        print("------------------------------------------ PARSER EXCEPTIONS ------------------------------------------")
        print("--------------------- ANALYZER ---------------------")

        for p_exception in context.status.parser_exceptions.analyzer_exceptions:
            print(p_exception)
        
        print("--------------------- EXTRACTOR ---------------------")
        for p_exception in context.status.parser_exceptions.extractor_exceptions:
            print(p_exception)
    
    except ContextNotCreatedException as e:
        print("Sorry, i can't create a context from the input you introduced")
        print(e)


    # try: 
    #     context.execution_result = execute(context)
    # except:
    #     pass

while(True):
    #selected_prompt = test_prompts[int(input(os.getenv("ASSISTANT") + ": (0-14) "))]  # Solicitar al usuario que ingrese un prompt para analizar.
    prompt = input("NOVA-02: ")
    chatbot(prompt)

"""
Input
↓
Preprocess
↓
Entity Extraction
↓
Context Generation
↓
Context Check
↓
Intent Execution
↓
Decision Engine
↓
Output

"""
