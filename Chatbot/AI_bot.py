from chatterbot import ChatBot
#this creates a chat bot for chatting
from chatterbot.trainers import ListTrainer
#this creates trainer for each language 
import os
#to read file from system
bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)
for files in os.listdir('path to data'):
    for file in os.listdir('path to data'+files):
        data=open('path to data'+files+'/' + file,'r',encoding="utf8").readlines()
        bot.train(data)
while True :
    message=input('You: ')
    if message.strip!='Bye' or message.strip!='bye': 
        reply=bot.get_response(message)
        print('Chatbot: ',reply)
    if message.strip=='Bye' or message.strip=='bye':
        print('Chatbot: Bye')
        break	
