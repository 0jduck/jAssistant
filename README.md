# jAssistant

A simple python wrapper made for the 'ollama' or 'open ai' api.
**Migh**t have issues with other api's so be careful.

Reads 'system.md' for the system prompt. If the file is not found then the system prompt will be an ampty string and a error is provided.
Reads the api config from '.env'. The file needs to have the following elements defined
* key - if an api key is needed
* model - the model to be requested
* url - the url to request from
* type - the type of api, e.x 'ollama', 'open ai' or other


