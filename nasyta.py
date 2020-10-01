import telebot
from telebot import types
import datetime
import time  
from pyowm import OWM
bot = telebot.TeleBot("1365221407:AAHwEPyig7KlENvA9sbXc50pMaHE4JwzZnw")


owm = OWM('c30a0f10eeb9a93501989842cfd6bb23', language = "RU")
cooldown = time.time()-120
cooldownnastya = time.time()-3000


@bot.message_handler(commands=['callfornastya'])
def callfornashya(message):
        global cooldownnastya
        MEMBER_ID = message.from_user.id
        GROUP_ID = message.chat.id
        name = message.from_user.first_name
        i=0
        if time.time() - cooldownnastya > 120:  
                bot.send_message(GROUP_ID, name+' ВЫЗЫВАЕТ НАСТЮ!')
                while(i<5):
                        bot.send_message(GROUP_ID, '@rwwct')
                        time.sleep(1)
                        i+=1
                cooldownnastya=time.time()

      

@bot.message_handler(commands=['weather'])
def weather(message):
        global cooldown
        GROUP_ID = message.chat.id
        place = owm.weather_at_place('Kyiv')
        wt = place.get_weather()
        if time.time() - cooldown > 120:  
                bot.send_message(GROUP_ID, 'Сегодня '+wt.get_detailed_status()+'\n'+str(round(wt.get_temperature('celsius')['temp']))+"°C🌡")
                cooldown = time.time()
 


bot.polling() 
