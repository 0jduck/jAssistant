# llm.py

# ---- file setup ----
# imports
from datetime import datetime
import requests
import json

from data import runtime

# ---- prompt ----
def sendPrompt(chat: list, api: dict = runtime.apiConfig) -> str:
    # validate data
    for key in api.keys():
        if api[key] == '':
            print(f'Bad .env file, {key} is empty')
            return 'Error'
    # stream
    if api['type'] == 'ollama' or api['type'] == 'open ai':
        stream = True
    else:
        stream = False
    # data
    headers = {
        "Authorization": f"Bearer {api['key']}",
        "Content-Type": "application/json"
    }
    payload = {
        'model': api['model'],
        'messages': chat,
        'stream': stream
    }
    # response
    response = requests.post(url=api['url'], headers=headers, json=payload, stream=stream)
    reply = ''
    if stream:
        if api['type'] == 'ollama':
            reply = streamOllama(response)
        if api['type'] == 'open ai':
            reply = streamOpenAi(response)
    else:
        reply = response.json()['message']['content']
    return reply

# ---- stream ----
def streamOllama(response) -> str:
    reply = ''
    for line in response.iter_lines(decode_unicode=True):
        if line:
            try:
                chunk = json.loads(line)
                text = chunk.get('message', {}).get('content', '')
                print(text, end='', flush=True)
                reply += text

                if chunk.get('done'):
                    break
            except json.JSONDecodeError:
                continue
    print(end='\n')
    return reply

def streamOpenAi(response) -> str:
    reply = ''
    for line in response.iter_lines(decode_unicode=True):
        if line:
            if line.startswith('data: '):
                line = line[6:]
            if line == '[DONE]':
                break

            try:
                chunk = json.loads(line)
                text = chunk.get('choices', [{}])[0].get('delta', {}).get('content', '') or ''
                print(text, end='', flush=True)
                reply += text
            except json.JSONDecodeError:
                continue
    print(end='\n')
    return reply

# ---- make chat ----
def makeChat(role: str, content: str, chat: list, system: str = runtime.systemPrompt):
    # add system prompt
    if len(chat) == 0:
        chatNew = [{'role': 'system', 'content': system}]
    else:
        chatNew = chat
    # add user prompt
    chatNew.append({'role': role, 'content': content})
    # update time in system prompt
    if chatNew and chatNew[0]['role'] == 'system':
        if '{time}' in chatNew[0]['content']:
            time = str(datetime.now()).split('.')[0]
            chatNew[0]['content'] = str(chatNew[0]['content']).replace('{time}', time)
    # return time
    return chatNew



