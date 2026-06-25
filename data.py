# data.py

# ---- file setup ----
# imports
from dotenv import load_dotenv
from pathlib import Path
import os

# ---- runtime data ----
class runtimeData:
    def __init__(self):
        load_dotenv('.env')
        self.apiConfig = {
            "model": os.getenv('model'),
            "url": os.getenv('url'),
            "type": os.getenv('type'),
            "key": os.getenv('key')
        }
        print(f'Running "{self.apiConfig["type"]}" with {self.apiConfig["model"]} on {self.apiConfig["url"]}')
        if Path('system.md').exists():
            self.systemPrompt = Path('system.md').read_text()
        else:
            self.systemPrompt = ''
            print('Found no system.md file so no systemprompt is set.')

runtime = runtimeData()

# ---- change runtime ----
def changeApiConfig(parts: list):
    if len(parts) > 0:
        load_dotenv('.env')
        for part in parts:
            if part  in runtime.apiConfig.keys():
                runtime.apiConfig[part] = os.getenv(part)
                if part != 'key':
                    print(f'Api config part {runtime.apiConfig[part]} is now updated')
    else:
        print('No changed api config parts, since none were inputed')

def changeSystemPrompt():
    if Path('system.md').exists():
        runtime.systemPrompt = Path('system.md').read_text()
    else:
        runtime.systemPrompt = ''
        print('Found no system.md file so no systemprompt is set.')


