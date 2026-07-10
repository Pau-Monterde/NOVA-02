from engine.models.exceptions.context_exceptions import ContextNotCreatedException, NotRootVerbInContextException
from engine.context_generator import generate_rcontext
from engine.models.context_model import RequestContext

def context_generation(prompt:str):
    print("Analizando el prompt: " + prompt)  # Mostrar el prompt seleccionado para análisis.

    context:RequestContext = generate_rcontext(prompt)  # Crear una instancia de Prompt con el texto ingresado.

    if not context.status.success:
        raise ContextNotCreatedException() 
    
    return context
    
def testing_chatbot(prompt:str):

    try:
        context:RequestContext = context_generation(prompt)
    

        print("------------------------------------------ LINGUISTIC ANALISYS ------------------------------------------")

        print("--------------------- POS ---------------------")
        for token in context.parsed_text.linguistic_analisys.pos:
            print(token.text + ": " + token.dep)

        print("--------------------- NER ---------------------")
        for ent in context.parsed_text.linguistic_analisys.ner:
            print(ent.text + ": " + ent.label)

        print("------------------------------------------ GRAMATICAL EXTRACTION ------------------------------------------")
        try: 
            rv = context.parsed_text.grammatical_extraction.root_verb.text
            if rv: 
                print("Root verb: " + rv)
        except NotRootVerbInContextException as e: print(e)

        try:
            do = context.parsed_text.grammatical_extraction.direct_object.text
            if do:
                print("Direct object: " + do)
        except: pass

        for in_obj in context.parsed_text.grammatical_extraction.indirect_objects:
            print("Object: " + in_obj.text)
            print("Object parent: " + in_obj.head_text)
        
        if not context.parsed_text.grammatical_extraction.indirect_objects:
            print("There aren't indirect objects in context")
        
        print("------------------------------------------ ROLES DETECTION ------------------------------------------")
        if context.role_frame:
            context.role_frame.show_roles()
        else: 
            print("There isn't any role assignment: ") 
            for se in context.status.semantic_exceptions:
                print(se)


        print("------------------------------------------ INTENT DETECTION ------------------------------------------")
        try:
            print(context.intent.rule.name)
        except Exception as e:
            print(context.status.fatal_exception)

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

def chatbot(prompt:str):
    try: 
        context:RequestContext = context_generation(prompt)
        print(context.intent.rule.name)
        print(context.intent.rule.execution(context))
    except ContextNotCreatedException as e:
        print("Sorry, i can't create a context from the input you introduced")
        print(e)
        return

while(True):
    #selected_prompt = test_prompts[int(input(os.getenv("ASSISTANT") + ": (0-14) "))]  # Solicitar al usuario que ingrese un prompt para analizar.
    prompt = input("NOVA-02: ")
    chatbot(prompt)




