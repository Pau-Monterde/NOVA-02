from engine.models.exceptions.context_exceptions import ContextNotCreatedException, NotRootVerbInContextException, PropmtIsNotCommandException
from engine.context_generator import generate_rcontext
from engine.models.context_model import RequestContext
from llm_manager import normalize_prompt, call_llm, generate_response 
from engine.models.history import ConversationHistory, HistoryEntry
from db import save_conversation, actualize_conversation

def context_generation(prompt:str, context_intents:list | None = None):
    context:RequestContext = generate_rcontext(prompt, context_intents)  # Crear una instancia de Prompt con el texto ingresado.

    if not context.status.success:
        raise ContextNotCreatedException() 
    
    return context

def chatbot(prompt:str, conversation_history:ConversationHistory, context_intents:list | None = None):
    normalized_prompt = normalize_prompt(prompt)
    print(normalized_prompt)

    try: 
        context:RequestContext = context_generation(normalized_prompt, context_intents)
        print("Demanda de skill detectada: " + context.intent.rule.name)

        try:
            print(context.intent.rule.name)
            phrase = context.intent.rule.execution(context)
        except Exception as e:
            print(e)
            raise PropmtIsNotCommandException()
        
        response = generate_response(phrase)
        print("NOVA-02: " + response)

        conversation_history.entry_list.append(HistoryEntry("assistant", response))
        return conversation_history, context
    
    except (ContextNotCreatedException, PropmtIsNotCommandException):
        response = call_llm(conversation_history.messages_list())
        print("NOVA-02: " + response)
        conversation_history.entry_list.append(HistoryEntry("assistant", response))
        
        return conversation_history, None
    
def main():
    conversation_history = ConversationHistory()
    fisrt_lap = True
    context_intents = []

    while(True):
        prompt = input("You: ")
        conversation_history.entry_list.append(HistoryEntry("user", prompt))

        if prompt.lower().strip() == "exit":
            print(f"Bye! Conversation history: {conversation_history.messages_list()}")
            return conversation_history

        conversation_history, context = chatbot(prompt, conversation_history, context_intents)
        
        if type(context) == RequestContext:
            if context.intent.rule.context_intents:
                context_intents = list(set(context_intents + context.intent.rule.context_intents))
                print(context_intents)

        if fisrt_lap == True:
            result = save_conversation(conversation_history)
            fisrt_lap = False
        
        else: 
            actualize_conversation(result, conversation_history)
main()

