
# Commands

## Prompt

Upload/publish prompt, in the same directory as the prompt:
``` prompter --prompt=ticketera.hbr --publish ```

## Embeddings
Upload text to semantic store aka embedings

Embeddings can be uploaded by running ```prompter --embed=<file> --collection=<collection-name> ``` in your terminal. Embeddings must be a text file, it supports Mark Down and Json.

you can specifiy chunkSize by running ```prompter --embed=<file> --collection=<collection-name> --chunkSize=<chunkSize>``` in your terminal. The default chunkSize is 1000.

```bash
prompter --embed=sinopsis.txt
```

## Querying Embeddings

Execute ```prompter``` then select Embeddings from menu.


# Setup Assistant

- [ ] Start ngrok tunnel to localhost:5000  ``` npx ngrok http 5000 ```
- [ ] Setup ngrok new tunnel URL https://3242-s...ngrok.io as the webhook URL for the Assistant in cinemark_ticketera.
- [ ] Upload prompt, run at the same directory as the prompt ``` prompter --prompt=ticketera.hbr --publish ```
- [ ] Create a new Assistant pointing to this prompt: ``` prompter ``` 
- [ ] Create a channel for the Assistant, and add the channel to the Assistant. ```prompter```


