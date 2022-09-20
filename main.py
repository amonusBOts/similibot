import random
import requests
import asyncio
from bs4 import BeautifulSoup as BS
from pprint import pprint
import urllib
from urllib.request import urlopen
from urllib.parse import quote as urlquote
from pyrogram import Client, filters
from pyrogram.types import Message, ReplyKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import CallbackQuery
import shutil
import os
import re
import urllib.request
import time
import json
import time
import random
from pyrogram import enums
from pyrogram.errors import BadRequest
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                            InlineKeyboardButton)
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

import validators
from config import Config as C
from s import get_sites as gs 
from s import tr

app = Client("bot", C.API_ID, C.API_HASH, bot_token=C.TOKEN)
@app.on_message(filters.private &  filters.command(["start"]))
async def start(bot, message):
  # global user_data
  # user_data[message.chat.id] = ''
  
  loop = asyncio.get_event_loop()
  await message.reply('با انتخاب حروف کلمات خود را بسازید')   



@app.on_inline_query()
async def answer(client, iq):


      print(iq)
      valid=validators.url((iq.query).strip())
      if valid==True:
        print("Url is valid")
        sites = gs(tr((iq.query).strip()))
        print(sites)
        if len(sites)<1:
            await iq.answer(
         results=[
            InlineQueryResultArticle(
                title="نتیجه ای یافت نشد",
                input_message_content=InputTextMessageContent(
                    """کاربر عزیز برای اینکه از ربات استفاده کنید باید لینک مناسب رو به عنوان کوئری در قسمت اینلاین وارد کنید
مثال:
✅```https://yjc.ir```
❌```yjc.ir```
❌```https://yjc```"""
                ),
                
                description="برای راهنمایی کلیک کنید"
                
            )
        ],
        cache_time=1
    )     
        else:

            results = []
            text = ''
            if len(sites.items())<30:

              for k,v in sites.items():
                  text+=f'{k}\n```{v}```\n\n'
            elif len(sites.items())>30:
              for k,v in sites.items():
                  text+=f'{k}\n'  

            results.append( InlineQueryResultArticle(
                    title='click to get all results',
                    input_message_content=InputTextMessageContent(
                        text
                    ),
                    description='all in one'
                    
                        
                    )
                )

             

            c = 0
            for k,v in sites.items():
                c+=1
                
                results.append( InlineQueryResultArticle(
                    title=k,
                    input_message_content=InputTextMessageContent(
                        v
                    ),
                    url="https://"+k,
                    description=f"",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton(
                                f"Open {k}",
                                url="https://"+k
                            )]
                        ]
                    )
                ))   

                if c==49:
                  break 

            await iq.answer(
                 results,
                cache_time=3
            )         
            

      else:
            print("Invalid url")
            await iq.answer(
             results=[
                InlineQueryResultArticle(
                    title="لینک وارد شده صحیح نیست",
                    input_message_content=InputTextMessageContent(
                        """کاربر عزیز برای اینکه از ربات استفاده کنید باید لینک مناسب رو به عنوان کوئری در قسمت اینلاین وارد کنید
    مثال:
    ✅```https://yjc.ir```
    ❌```yjc.ir```
    ❌```https://yjc```"""
                    ),
                    
                    description="برای راهنمایی کلیک کنید",
                    
                )
            ],
            cache_time=1
        )     


          



































  
if __name__ == '__main__':
    print('[Bot] : listening :)')
    app.run()




