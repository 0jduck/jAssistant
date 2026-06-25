# main.py

# ---- file setup ----
# imports
from datetime import datetime
from sys import argv
from api import (
    makeChat,
    prompt
)

# variables
running = True
debugMode = False
if '-d' in argv:
    debugMode = True

# ---- debug ----
def debug(*args):
    if debugMode:
        for arg in args:
            print(repr(arg))

# ---- make input ----
def makePrompt(prompt: str) -> str:
    time = str(datetime.now()).split('.')[0]
    promptNew = f'[Time: {time}]User: {prompt}'
    return promptNew

# ---- run file ----
if __name__ == '__main__':
    chat = []
    try:
        while running:
            userInput = input('> ')
            if userInput.startswith('/'):
                pass
            else:
                userPrompt = makePrompt(prompt=userInput)
                chat = makeChat(role='user', content=userPrompt, chat=chat)
                debug(chat)
                reply = prompt(chat=chat)
                chat = makeChat(role='assistant', content=reply, chat=chat)
    except KeyboardInterrupt:
        pass

