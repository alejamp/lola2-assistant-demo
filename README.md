
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



## Repositories

[lolapy](https://github.com/alejamp/lola-py-sdk)
[prompter-cli](https://github.com/alejamp/prompter-cli)
