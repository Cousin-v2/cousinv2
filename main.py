import asyncio
import os

os.system('pip install -U uvloop')

import uvloop
import sys

if not os.getenv('DEVICE_ID') and \
        not os.getenv('ACCOUNT_ID') and \
        not os.getenv('SECRET'):
    print("Please paste your device auths into the \".env\" file.\n")
    sys.exit()

os.system('pip install -U FNBOT2')
os.system('clear')

import FNBOT2

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

client = FNBOT2.Partybot(
    device_id=os.getenv('DEVICE_ID'),
    account_id=os.getenv('ACCOUNT_ID'),
    secret=os.getenv('SECRET')
)

try:
    client.run()
except Exception as e:
    print(e)
    print("Can't login because your device auths is probably wrong.")
