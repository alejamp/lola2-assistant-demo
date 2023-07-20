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


