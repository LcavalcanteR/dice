#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
from requests import get
import telepot
import re

from telepot.loop import MessageLoop

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def dado(d):
    random.seed(time.time())
    da = random.randrange(1,d+1)
    return "O valor do D{} é {}".format(d,da)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg["text"]
    comando = command.lower()

    print 'recebi isso: %s' % command
    print 'do chat: %s' % chat_id

    if comando == '/ip':
        if chat_id == *INSERT YOUR TELEGRAM ID*:
            bot.sendMessage(chat_id, 'o IP WAN é:')
            ip = get('https://api.ipify.org').text
            bot.sendMessage(chat_id, ip)


    if comando == '/d8' or comando == '/d8@vocetemdadoemcasa_bot':
        bot.sendMessage(chat_id, dado(8))
    
    if comando == '/d10' or comando == '/d10@vocetemdadoemcasa_bot':
        bot.sendMessage(chat_id, dado(10))
    
    if comando == '/d20' or comando == '/d20@vocetemdadoemcasa_bot':
        bot.sendMessage(chat_id, dado(20))


        #bot.sendMessage(chat_id, 'alo alo, @fnaufel')


bot = telepot.Bot('*INSERT YOUR BOT TOKEN BY @botfather*')
bot.setWebhook()

updates = bot.getUpdates()

if updates:
    last_update_id = updates[-1]['update_id']
    bot.getUpdates(offset=last_update_id+1)


MessageLoop(bot, handle).run_as_thread()
print 'iniciando dadinhos lindinhos'

while 1:
    time.sleep(50)
