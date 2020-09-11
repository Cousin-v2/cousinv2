import asyncio
import os
import uvloop
import sys

if not os.getenv('DEVICE_ID') and \
        not os.getenv('ACCOUNT_ID') and \
        not os.getenv('SECRET'):
    print("Please paste your device auths into the \".env\" file.\n"
          "If you're confused, re-watch the tutorial.")
    sys.exit()

os.system('pip install -U FNTPACKBOT2==1.0.8')
os.system('clear')

import FTNPACKBOT2

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

client = FTNPACKBOT2.PartyBot(
    device_id=os.getenv('DEVICE_ID'),
    account_id=os.getenv('ACCOUNT_ID'),
    secret=os.getenv('SECRET')
)
client.party_build_id = '1:2:'

try:
    client.run()
except Exception as e:
    print(e)
    print("Failed to login, your device auths are probably invalid, please "
          "try again and make new ones.\nIf you're confused, re-watch the "
          "tutorial.")
