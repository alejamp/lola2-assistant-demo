# Lola2 - Assistant Examples

### Requirements

Install lolapy from git using pip

```bash
pip install "git+https://github.com/alejamp/lola-py-sdk.git"
```

### Install dependencies

```bash
npm install -g prompter-cli
```

set env variables

```bash
export PROMPTER_SERVER_URL=[PROMPTER_SERVER_URL]
```

Then execute ```prompter``` and select Login. Use your username and password.

### Create a new assistant and channel


### Publish a prompt

Publish a prompt by running `prompter --prompt=<prompt> --publish` in your terminal. Note that the prompt must be a valid Handlebars template. See [Handlebars](https://handlebarsjs.com/) for more information.
If no promptId is provided, the file name will be used as the promptId. If the prompt is already published, it will be updated.


