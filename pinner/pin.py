#!/home/test/pinner/bin/python3

import time
import random
import urllib3

import telepot


chatid = -10000000000000
token = ''

bot = telepot.Bot(token)

def handle(msg):
    global chatid
    content_type, message_id, chat_id = telepot.glance(msg)

    if content_type == "text":
        if chat_id == chatid:
          
            #Watch errors without fall
            try:
            
                #Pin without notify
                if msg["text"][0:4] == "/pin":
                    bot.pinChatMessage(chat_id,
                                       msg["reply_to_message"]["message_id"],
                                       disable_notification=True)              
                
                #Pin with notify
                if msg["text"][0:11] == "/pin notify":
                    bot.pinChatMessage(chat_id,
                                       msg["reply_to_message"]["message_id"],
                                       disable_notification=False)

                #Easter egg
                if msg["text"][0:4] == "/ban":
                    if random.choice([0, 1]) == 0:
                        bot.kickChatMember(chat_id, msg["from"]["id"])
                    else:
                        print("Lucky")

            except Exception as ex:
                print(ex)
                pass


bot.message_loop(handle)


while 1:
    time.sleep(10)
