import asyncio
import os
import sys
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

os.system('pip install -U FNBOT2')
os.system('clear')

import FNBOT2

client = FNBOT2.PartyBot(
  device_id=os.getenv('DEVICE_ID'),
  account_id=os.getenv('ACCOUNT_ID'),
  secret=os.getenv('SECRET')
)

try:
    client.run()
except Exception as e:
    print(e)
    print("Can't login because your device auths is probably wrong.")
