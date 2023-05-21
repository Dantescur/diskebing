import datetime
import json

import pytz
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import logging
import time
from sydney import SydneyClient
from time import sleep

sleep(1200)





with open('package.json') as json_file:
    data = json.load(json_file)
api_id = data['api_id']
api_hash = data['api_hash']

strings = str(data['session'])





client = TelegramClient(StringSession(strings), api_id, api_hash)
client.start()



usuarios=[775593292]



bingcookie="1Gj7ErpU5U4GhgpMvf3dBEFSStqGtuMhEM3rX6s09gP8D7p5UeUXH5WEPGSx3YnsVXFxP-OjbXYZzDaK9am83nPvcJr7yqP57RuwXKezw-yaqE_wE5O-OMRzjqSSIv0cxs2vw-ReMf9aRMSVgiCATKSmcW9YaKv-ZjXwZ7pIdIwOPgcpwnL444rF_MTgUtAHPIiRKoJrt3BEmna_l_-TTDztCO9OgN23R-BelQlNbwh0"

async def bingbot(prompttext=None,event=None,mode='creative') -> None:
    async with SydneyClient(mode,bing_u_cookie=bingcookie) as sydney:
        #while True:

            prompt = prompttext

            if prompt == "!reset":
                await sydney.reset_conversation()




            resp=""
            await event.edit("...thinking...")
            response = await sydney.ask(prompt, citations=False)
            await event.edit(response)
            await sydney.reset_conversation()


@client.on(events.NewMessage(pattern="!tk",from_users=usuarios))
async def forward_to_channel(event):
    prompt=str(event.raw_text).replace('!tk','')
    flag=True
    if prompt.startswith('balanced') or prompt.startswith('precise'):
        mode=prompt.split()[0]
        prompt=prompt.replace(mode,'')
        while flag:
            try:
             await bingbot(prompt,event,mode)
             flag=False

            except Exception as e:
                pass

    while flag:
        try:
            await bingbot(prompt,event)
            flag=False

        except Exception as e:
           pass






client.run_until_disconnected()