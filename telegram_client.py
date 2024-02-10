# telegram_client.py
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

def authenticate_client(api_id, api_hash, phone):
    client = TelegramClient(phone, api_id, api_hash)
    client.connect()
    
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))
    
    return client

def fetch_dialogs(client):
    result = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=200,
        hash=0
    ))
    
    chats = [chat for chat in result.chats if getattr(chat, 'megagroup', False)]
    return chats
