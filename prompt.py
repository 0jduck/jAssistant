# prompt.py

# ---- file setup ----
# imports
from datetime import datetime

# ---- make prompt ----
def makePrompt(prompt: str) -> str:
    time = str(datetime.now()).split('.')[0]
    promptNew = f'[Time: {time}]User: {prompt}'
    return promptNew

