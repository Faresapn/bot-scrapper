from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time
import os
api_id = 18896359
api_hash = 'dd3c92597fa82ca4a8f594c8c661a961'

cwd = os.getcwd()
 
print(f"[*] Automation Scraping Member Group Telegram!\n[*] Author: RJD")
target = input(f"[*] Input Link/@ Group (example: @defiandmore): ")

try:
    client = TelegramClient('sess', api_id, api_hash)

    client.connect()
    if not client.is_user_authorized():
        phone = input(f"[*] Input Number (example: +6213232323232): ")
        client.send_code_request(phone)
        client.sign_in(phone, input('[*] Enter the code: '))

    print('[*] Fetching Members...')
    all_participants = []
    cwd = os.getcwd()
    list_member = []
    try:

        all_participants = client.iter_participants(target)
        print('[*] Get Member...')
        
        i = 0
        for user in all_participants:
            if user.username:
                username = user.username
                list_member.append(username)
                i = i + 1
    
        print(f'[*] {i} Members scraped successfully.')
    except Exception as e:
        pass
    cwd = os.getcwd()
    msg = "message.txt"
    msg = open(f"{cwd}\\{msg}","r",encoding='utf-8')
    msg = msg.read()
    for i in list_member:
        try:
            result =  client.send_message(f'{i}',f'{msg}')
            print(f"[{time.strftime('%d-%m-%y %X')}] [ {i} ] [ Successfully sent ]")
            time.sleep(30)
        except Exception as e:
            print(f"[{time.strftime('%d-%m-%y %X')}] [ {i} ] [ {e} ]!")
        time.sleep(3)

except:
    pass
 
