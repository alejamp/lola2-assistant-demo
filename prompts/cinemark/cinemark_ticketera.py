import threading
import time
from lolapy import LolaSDK
from lolapy import LolaContext
from tokens import SUNDEVS_CINEMARK_TICKETERA_TOKEN
import schedule

lola = LolaSDK(
    lola_token=SUNDEVS_CINEMARK_TICKETERA_TOKEN, 
    prompter_url='https://lola-dev-v2.ue.r.appspot.com/',
    webhook_url='https://3ebb-181-168-225-209.ngrok-free.app')






@lola.on_command('get_billboard')
def handle_get_cryptocurrency_price(session, ctx: LolaContext, request):
    city = request['data']['args']['city']
    movie = request['data']['args']['movie']

    # TODO: Get billboard from Cinemark API from that city

    # Save into state the current city
    s = ctx.state.get()
    s['city'] = city
    ctx.state.set(s)

    return {'data': f'Please select a theater:\nAvailable theaters: Cinemark Plaza Nor, Cinemark Floresta'}


@lola.on_command('get_billboard_for_a_theater')
def handle_get_billboard_for_a_theater(session, ctx: LolaContext, request):
    name = request['data']['args']['name']
    
    # TODO: Get billboard from Cinemark API from that city

    # Save into state the current city
    s = ctx.state.get()
    s['theater'] = name
    ctx.state.set(s)

    return {'data': f'Movies:\n-Barbie\n Showtime: 18:00, 20:00, 22:00'}

@lola.on_command('do_checkout')
def handle_do_checkout(session, ctx: LolaContext, request):
    theater = request['data']['args']['theater']
    movie = request['data']['args']['movie']
    showtime = request['data']['args']['showtime']
    
    # TODO: Get billboard from Cinemark API from that city

    # Save into state the current city
    # s = ctx.state.get()
    # s['theater'] = name
    # ctx.state.set(s)

    return {'data': f'Your ticket has been bought!'}


@lola.on_event('onTextMessage')
def handle_text_message(session, ctx: LolaContext, msg):
    
    print(f'Got text message: {msg["text"]}')
    s = ctx.state.get()
    print(f'Current state: {s}')
    ctx.state.set({'counter': s.get('counter', 0) + 1})

    ctx.timeout.set(session, ctx, 5, '5_seconds_without_message')

    # Testing send message to client
    # This message will be sent to the client
    # But it will not interrupt the flow to the AI
    # Use this to send messages to the client without interrupting the flow
    # ctx.messanger.send_text_message(f'You said1: {msg["text"]}') 

    # Testing send message to client
    # This message will be sent to the client
    # And it will interrupt the flow to the AI
    # return f'You said2: {msg["text"]}'


@lola.on_timeout()
def handle_timeout(session, ctx: LolaContext, label):
    print(f'Timeout reached for label: {label}')
    ctx.messanger.send_text_message(f'Timeout reached for label: {label}')

# On each new conversation, this event will be triggered
# This is useful to initialize the state of the conversation
@lola.on_event('onNewConversation')
def handle_new_conversation(session, ctx: LolaContext, msg):
    
    print(f'Got new conversation message: {msg["text"]}')

    # Get the current state
    s = ctx.state.get()
    print(f'Setting default city as Cali')
    s['city'] = "Cali"

    s['watched_movies'] = [
        'Lo que el viento se llevó',
        'El Padrino',
        'El Padrino II',
        'El Padrino III',
        'Titanic'
    ]
    ctx.state.set(s)
    

    # Set the current state, account_balance will be 100 if it does not exist
    ctx.state.set({'account_balance': s.get('account_balance', 100)})

    # This return will be sent to the client and will interrupt the flow to the AI
    # Uncomment this if you want to send a message to the client without AI intervention
    # return f'You said: {msg["text"]}'





lola.listen()
