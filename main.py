# main.py

# ---- file setup ----
# imports
from sys import argv

from prompt import makePrompt
from api import (
    makeChat,
    sendPrompt
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
                reply = sendPrompt(chat=chat)
                chat = makeChat(role='assistant', content=reply, chat=chat)
    except KeyboardInterrupt:
        pass

