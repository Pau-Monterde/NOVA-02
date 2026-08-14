from engine.models.exceptions.context_exceptions import (
    ContextNotCreatedException,
    NotRootVerbInContextException,
    PromptIsNotCommandException
)

from engine.context_generator import generate_rcontext
from engine.models.context_model import RequestContext
from engine.models.queues_model import EngineQueues

from llm_manager import (
    normalize_prompt,
    call_llm,
    generate_response
)

from engine.models.history import (
    ConversationHistory,
    HistoryEntry
)

from db import (
    save_conversation,
    actualize_conversation,
    save_user,
    get_user
)

from engine.models.user_model import UserData

from ui.ui import user_interface
from ui.api import Api

import threading
from queue import Queue

def context_generation(prompt: str, context_intents: list | None = None):
    context: RequestContext = generate_rcontext(prompt, context_intents)

    if not context.status.success:
        raise ContextNotCreatedException()

    return context

def chatbot(conversation_history: ConversationHistory, engine_queues:EngineQueues, context_intents: list | None = None):

    # Cogemos el siguiente mensaje del buzón
    prompt:str = engine_queues.input_queue.get()
    print(get_user().alias + ": " +  prompt)

    conversation_history.entry_list.append(HistoryEntry("user", prompt))

    if prompt.lower().strip() == "exit":
        print(
            f"Bye! Conversation history: "
            f"{conversation_history.messages_list()}"
        )

        return conversation_history, None

    normalized_prompt = normalize_prompt(prompt)

    print(normalized_prompt)

    try:

        context:RequestContext = context_generation(normalized_prompt, context_intents)

        print("Demanda de skill detectada: " + context.intent.rule.name)

        try:
            print(context.intent.rule.name)

            context = context.intent.rule.execution(context)

        except Exception as e:
            print(e)
            raise PromptIsNotCommandException()

        context.response = generate_response(context.response_raw)
        engine_queues.response_queue.put(context.response)

        conversation_history.entry_list.append(HistoryEntry("assistant", context.response))

        return conversation_history, context

    except (ContextNotCreatedException, PromptIsNotCommandException):
        response = call_llm(conversation_history.messages_list())
        engine_queues.response_queue.put(response)

        conversation_history.entry_list.append(HistoryEntry("assistant", response))

        return conversation_history, None

def engine(engine_queues:EngineQueues):
    print("ENGINE ACTIVATED")

    user_data: UserData = get_user()
    print(user_data.username)

    conversation_history = ConversationHistory()
    first_lap = True
    context_intents = []

    while True:
        conversation_history, context = chatbot(conversation_history, engine_queues, context_intents)

        if type(context) == RequestContext:
            if context.intent.rule.context_intents:
                context_intents = list(set(context_intents + context.intent.rule.context_intents))

        if first_lap:
            result = save_conversation(conversation_history)
            first_lap = False

        else:
            actualize_conversation(result, conversation_history)

        print("ENGINE WORKING")

def main():

    # Creamos el buzón
    engine_queues = EngineQueues()

    # Creamos el hilo del engine
    engine_thread = threading.Thread(target=engine, args=(engine_queues,))

    # Arrancamos el engine
    engine_thread.start()

    api = Api(engine_queues)

    engine_queues.input_queue.put("Hola, que tal?")

    user_interface(api, engine_queues)
    
main()