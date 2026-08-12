from engine.models.exceptions.context_exceptions import (
    ContextNotCreatedException,
    NotRootVerbInContextException,
    PropmtIsNotCommandException
)

from engine.context_generator import generate_rcontext
from engine.models.context_model import RequestContext

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

import threading
from queue import Queue


def context_generation(prompt: str, context_intents: list | None = None):
    context: RequestContext = generate_rcontext(prompt, context_intents)

    if not context.status.success:
        raise ContextNotCreatedException()

    return context

def chatbot(conversation_history: ConversationHistory, input_queue: Queue, context_intents: list | None = None):

    # Cogemos el siguiente mensaje del buzón
    prompt = input("You: ")

    conversation_history.entry_list.append(HistoryEntry("user", prompt))

    if prompt.lower().strip() == "exit":
        print(
            f"Bye! Conversation history: "
            f"{conversation_history.messages_list()}"
        )

        return conversation_history

    normalized_prompt = normalize_prompt(prompt)

    print(normalized_prompt)

    try:

        context: RequestContext = context_generation(normalized_prompt, context_intents)

        print("Demanda de skill detectada: " + context.intent.rule.name)

        try:
            print(context.intent.rule.name)

            context = context.intent.rule.execution(context)

        except Exception as e:
            print(e)
            raise PropmtIsNotCommandException()

        context.response = generate_response(context.response_raw)

        print("NOVA-02: " + context.response)

        conversation_history.entry_list.append(HistoryEntry("assistant", context.response))

        return conversation_history, context

    except (ContextNotCreatedException, PropmtIsNotCommandException):

        response = call_llm(conversation_history.messages_list())

        print("NOVA-02: " + response)

        conversation_history.entry_list.append(HistoryEntry("assistant", response))

        return conversation_history, None


def engine(input_queue: Queue):
    print("ENGINE ACTIVATED")

    user_data: UserData = get_user()

    if not user_data:
        print("No hay user")

    else:
        print(user_data.username)

    conversation_history = ConversationHistory()
    first_lap = True
    context_intents = []

    while True:
        conversation_history, context = chatbot(conversation_history, input_queue, context_intents)

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
    input_queue = Queue()

    # Creamos el hilo del engine
    engine_thread = threading.Thread(target=engine,args=(input_queue,))

    # Arrancamos el engine
    engine_thread.start()

    # Prueba temporal:
    # input_queue.put("hola")

    # Más adelante:
    # user_interface()
main()