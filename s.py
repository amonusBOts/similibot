
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


from FakeAgent import Fake_Agent
fa = Fake_Agent()
request_headers= {
  "User-Agent": fa.random()

  }









# r = requests.get(url, allow_redirects=True, timeout=5, headers=request_headers)
# # print(r.content)
# soup = BS(r.content, 'html.parser')  
# sites = soup.find_all('div',class_ = "row")
# sitre_lst = {}
# for i in sites :
#      try:
#        print(i.a['href'].replace('/',''))
#        print(i.find('p').text.strip())
#        print('\n\n------\n\n')
#        if i.a['href'].replace('/','') not in sitre_lst:
#           sitre_lst[i.a['href'].replace('/','')] = i.find('p').text.strip()
#      except:
#       pass  




# for k,v in sitre_lst.items():
#    print(k)
#    print('description : ',v)
    
#    print('\n\n')   







def get_sites(url) :
   r = requests.get("https://xranks.com/alternative/"+url, allow_redirects=True, timeout=5, headers=request_headers)
   soup = BS(r.content, 'html.parser')  
   sites = soup.find_all('div',class_ = "row")
   sitre_lst = {}
   for i in sites:
        try:
          print(i.a['href'].replace('/',''))
          print(i.find('p').text.strip())
          print('\n\n------\n\n')
          if i.a['href'].replace('/','') not in sitre_lst:
             sitre_lst[i.a['href'].replace('/','')] = i.find('p').text.strip()
        except:
         pass  




   for k,v in sitre_lst.items():
      print(k)
      print('description : ',v)
       
      print('\n\n') 
   return sitre_lst   






# a = get_sites('https://xranks.com/alternative/onehack.us')     
# print(a)
import validators
link = 'https://takporn.com'

def tr(link):
   l = link.split('/')[2]
   print(l[2])
   return l

valid=validators.url('https://takporn.com')
if valid==True:
        print("Url is valid")



