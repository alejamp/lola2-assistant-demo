from lolapy import LolaSDK
from lolapy import LolaContext
from tokens import LOLA_TOKEN_DEMO

lola = LolaSDK(
    lola_token=LOLA_TOKEN_DEMO, 
    prompter_url='https://lola-dev-v2.ue.r.appspot.com/',
    webhook_url='https://5cf3-181-168-225-209.ngrok-free.app')


@lola.on_command('get_cryptocurrency_price')
def handle_get_cryptocurrency_price(lead, ctx: LolaContext, cmd):
    cryptocurrency = cmd['data']['args']['cryptocurrency']
    currency = cmd['data']['args']['currency']

    # dict with data to return to Lola
    prices = {
        'ETH': 600,
        'BTC': 20000,
        'LTC': 100,
        'ADA': 1.5
    }

    # return {'data': prices}

    ctx.messanger.send_typing_action()
    ctx.messanger.send_text_message(f'Hola amiguito')

    # if cryptocurrency is not in prices, return error
    if cryptocurrency not in prices:
        return {'data': f'Cryptocurrency {cryptocurrency} not supported'}

    return {'data': f'{cryptocurrency} price in {currency} is {prices[cryptocurrency]}'}




@lola.on_event('onTextMessage')
def handle_text_message(lead, ctx: LolaContext, msg):
    
    print(f'Got text message: {msg["text"]}')
    s = ctx.state.get()
    print(f'Current state: {s}')
    ctx.state.set({'counter': s.get('counter', 0) + 1})

    # Testing send message to client
    # This message will be sent to the client
    # But it will not interrupt the flow to the AI
    # Use this to send messages to the client without interrupting the flow
    # ctx.messanger.send_text_message(f'You said1: {msg["text"]}') 

    # Testing send message to client
    # This message will be sent to the client
    # And it will interrupt the flow to the AI
    # return f'You said2: {msg["text"]}'

    if msg['text'].lower() == 'ping':
        return 'pong'
    



# On each new conversation, this event will be triggered
# This is useful to initialize the state of the conversation
@lola.on_event('onNewConversation')
def handle_new_conversation(lead, ctx: LolaContext, msg):
    
    print(f'Got new conversation message: {msg["text"]}')

    # Get the current state
    s = ctx.state.get()
    print(f'Current state: {s}')

    # Set the current state, account_balance will be 100 if it does not exist
    ctx.state.set({'account_balance': s.get('account_balance', 100)})

    # This return will be sent to the client and will interrupt the flow to the AI
    # Uncomment this if you want to send a message to the client without AI intervention
    # return f'You said: {msg["text"]}'




lola.listen()
