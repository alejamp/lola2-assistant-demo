
<p align="center">
  <img src="https://firebasestorage.googleapis.com/v0/b/numichat.appspot.com/o/Perf_Lola%2BH.way%20banner.png?alt=media&token=8a0dac42-1f76-4754-ac9c-40a93ba02125" alt="Logo">
</p>

# Lola2 - Assistant Examples

### Requirements

Python 3.8 or higher

Install **lolapy** from git using pip

```bash
pip install "git+https://github.com/alejamp/lola-py-sdk.git"
```

### Install Prompter CLI Tool

```bash
npm install -g prompter-cli
```

set env variables for prompter server url

```bash
export PROMPTER_SERVER_URL=[PROMPTER_SERVER_URL]
```

Then execute ```prompter``` and select Login. Use your username and password.

#### Create Assistant

Execute ```prompter``` then from menu select Assistant -> Create New. Input the assistant name and description. Keep `lola` as agent.

#### Create a telegram channel

Execute ```prompter``` then from menu select Channel -> Register New. Then input the token.

### Publish a prompt

Publish a prompt by running `prompter --prompt=<prompt> --publish` in your terminal. Note that the prompt must be a valid Handlebars template. See [Handlebars](https://handlebarsjs.com/) for more information.
If no promptId is provided, the file name will be used as the promptId. If the prompt is already published, it will be updated.


### Configure Assistant into lolapy

This project requires a token.py file, which contains the following variables:

```python

# Telegram channel: https://t.me/[bot_name]
LOLA_TOKEN_CTOS = "..."

# Telegram channel: https://t.me/[bot_name]
LOLA_TOKEN_DEMO = "..."

# Telegram channel: https://t.me/[bot_name]
SUNDEVS_CINEMARK_TICKETERA_TOKEN = "..."
```
If you have already created the assistant, you can get the tokens from the prompter-cli tool. Execute `prompter` then from menu select Assistant -> Select, then select the assistant and select View Info. The tokens will be displayed.


## Prompts

Lola2 utilizes [Handlebars](https://handlebarsjs.com/) templates to generate prompts. The output is a HTML like named PML, Prompt Markup Language. The PML is then rendered on each customer's message using a context object.

VS Code has a handlebars extension that can be used for syntax highlighting and snippets. Check recommended extensions for this project.

Prompts context variables are:
- date: current date
- state: current conversation state. This is an object that contains any assistant implementation related data. For example, if the assistant is a ticketing assistant, the state may contain the selected movie, the selected seats, etc.
- message: the customer's last message to the assistant. Useful for embeddings queries.

In handlebars, you can use the `{{#if}}` helper to conditionally render a block. For example, if you want to render the customer's name if the state variable `name` exists.

```handlebars
{{#if state.name}}
The customer's name is {{state.name}}
{{/if}}
```

Conditionals do not supports operations, so you can't do something like `{{#if state.name == 'John'}}`. 
In future versions, we will add support for operations.

## Repositories

[lolapy](https://github.com/alejamp/lola-py-sdk)
[prompter-cli](https://github.com/alejamp/prompter-cli)
