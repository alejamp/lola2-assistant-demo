from lolapy import LolaSDK
from lolapy import LolaContext
from tokens import LOLA_TOKEN_CTOS
import threading


lola = LolaSDK(
    lola_token=LOLA_TOKEN_CTOS, 
    prompter_url='https://lola-dev-v2.ue.r.appspot.com/',
    webhook_url='https://1d29-181-168-225-209.ngrok-free.app')

def do_simething_heavy_async(ctx: LolaContext, seconds=10):
    print(f'Doing something heavy for {seconds} seconds')
    import time
    time.sleep(seconds)
    print('Something heavy is done!')
    ctx.messanger.send_typing_action()
    time.sleep(5)
    ctx.messanger.send_text_message('Something heavy is done!')


@lola.on_command('add_contact')
def handle_add_contact(lead, ctx: LolaContext, request):
    name = request['data']['args']['name']
    phone = request['data']['args']['phone']
    email = request['data']['args'].get('email', None)

    s = ctx.state.get()
    print(f'Current state: {s}')

    # Add contact 
    ctos = s.get('contacts', [])
    ctos.append({'name': name, 'phone': phone, 'email': email})
    ctx.state.set({'contacts': ctos})

    return "Done!"



@lola.on_command('remove_contact')
def handle_remove_contact(lead, ctx: LolaContext, request):
    name = request['data']['args']['name']

    s = ctx.state.get()
    print(f'Current state: {s}')

    # Get contacts
    ctos = s.get('contacts', [])
    
    # Remove contact
    ctos = [c for c in ctos if c['name'].lower() != name.lower()]

    ctx.state.set({'contacts': ctos})

    return "Done!"


@lola.on_event('onTextMessage')
def handle_text_message(lead, ctx: LolaContext, msg):
    print(f'Got text message: {msg["text"]}')

    if msg['text'].lower() == 'ping':
        return 'pong'
    
    # Do something heavy without blocking execution
    threading.Thread(target=do_simething_heavy_async, args=(ctx,5)).start()


@lola.on_event('onError')
def handle_errors(lead, ctx: LolaContext, msg):
    
    print(f'Message: {msg["message"]}')
    print(f'Error: {msg["error"]}')

    if msg['text'].lower() == 'ping':
        return 'pong'
    
# On each new conversation, this event will be triggered
# This is useful to initialize the state of the conversation
@lola.on_event('onNewConversation')
def handle_new_conversation(lead, ctx: LolaContext, msg):
    
    print(f'Got new conversation message: {msg["text"]}')

    ctx.messanger.send_text_message(f'Welcome friend!!!', True) 




lola.listen()
