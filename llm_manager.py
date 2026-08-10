import requests
import json
from engine.models.history import ConversationHistory

def normalize_prompt(phrase:str):
    prompt = f"""
        You are a text normalizer.

        Rewrite the following text while preserving its exact meaning.

        Input: {phrase}

        Rules:
        - Return ONLY the rewritten text.
        - Do not explain anything.
        - Do not answer the request.
        - Do not add descriptive words (such as "application", "browser", "website", etc.).
        - Do not remove any existing words unless required by grammar.
        - Insert articles (the, a, an) only when they make the sentence more natural.
        - Preserve commands as commands.
        - Preserve questions as questions.
        - Correct grammar only.
        - Output exactly one sentence.

        Examples:

        open spotify
        Open the Spotify.

        close chrome
        Close the Chrome.

        play music
        Play the music.

        open the spotify
        Open the Spotify.

        what is a push up
        What is a push-up?

        explain what is a push up
        Explain what a push-up is.
    """
    

    resp = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.8
        }
    },
    timeout=30,
    )

    resp.raise_for_status()
    return resp.json()["response"].strip()

def call_llm(messages, temperature:float = 0.8) -> str:
    resp = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "gemma3:1b",
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": temperature
        }
    },
    timeout=30,
)
    resp.raise_for_status()
    return resp.json()["message"]["content"].strip()

def generate_response(phrase:str) -> str:

    prompt = f"""
        You are going to receive INSTRUCTIONS about what a response must say.
        This is NOT a user message asking you something: it is an order stating
        what text you must produce. Do not comment on the instructions, do not
        greet them, do not reply to them as if it were a conversation. Your only
        task is to GENERATE the final text that someone else will read.

        INSTRUCTIONS:
        Original sentence: "{phrase}"
        - Rewrite it as a single short, clear, grammatically correct sentence in
        neutral English.
        - Fix spelling errors and remove filler words.
        - Do not add new information
        or change the meaning.
        - Do not include intros like "Sure, here you go" or quotation marks.
        - Variate the words and structure to make it sound more natural and fluent, but keep the meaning intact.

        FINAL TEXT TO SAY (start directly, no preamble):
    """
    

    resp = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "gemma3:1b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.8
        }
    },
    timeout=30,
    )

    resp.raise_for_status()
    return resp.json()["response"].strip()

def detect_speech_act(phrase:str):
    prompt = f"""
    You are a speech act classifier.

    Your task is to classify the user's message into EXACTLY ONE of the following categories:

    - EXECUTION
    - INFORMATION
    - EXPLANATION
    - CONVERSATION
    - CONFIRMATION
    - CLARIFICATION
    - CORRECTION
    - FEEDBACK
    - UNKNOWN

    Definitions:

    EXECUTION
    The user wants the assistant to perform an action.
    Examples:
    - Open Spotify
    - Send this file to John
    - Close Chrome
    - Play some music

    INFORMATION
    The user asks for factual information or requests data.
    Examples:
    - What time is it?
    - What's the weather?
    - Who is Elon Musk?
    - How much RAM do I have?

    EXPLANATION
    The user wants an explanation, description, or understanding of something.
    Examples:
    - How does Arch Linux open programs?
    - Explain TCP.
    - Why is the sky blue?

    CONVERSATION
    General conversation, greetings, chit-chat or casual interaction.
    Examples:
    - Hi
    - Hello
    - How are you?
    - Tell me a joke

    CONFIRMATION
    The user confirms, accepts, rejects or answers a previous question.
    Examples:
    - Yes
    - No
    - Sure
    - Go ahead
    - Cancel it

    CLARIFICATION
    The user clarifies a previous message or specifies what they meant.
    Examples:
    - Spotify, not Chrome.
    - The first one.
    - That PDF.
    - I meant my desktop.

    CORRECTION
    The user corrects previous information.
    Examples:
    - No, that's wrong.
    - I said Spotify.
    - Actually, I meant Firefox.

    FEEDBACK
    The user evaluates or reacts to the assistant's response.
    Examples:
    - Thanks.
    - Perfect.
    - That wasn't helpful.
    - Great job.

    UNKNOWN
    Use only if none of the above categories clearly apply.

    Rules:
    - Return ONLY the category name.
    - Do NOT explain your reasoning.
    - Do NOT output punctuation.
    - Do NOT output quotes.
    - Do NOT output multiple categories.
    - Your response must contain exactly one word from the list above.

    User message:
    "{phrase}"

    """
    

    resp = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.8
        }
    },
    timeout=30,
    )

    resp.raise_for_status()
    return resp.json()["response"].strip()

