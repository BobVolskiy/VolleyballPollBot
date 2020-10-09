import telebot
from telebot import types
import datetime
import time  
from pyowm import OWM
timing = time.time()-45000 
bot = telebot.TeleBot("1381051273:AAHATq_xhk-piS6dU2Txv2P6POGor5pNoOs")
options = ["Могу", "50/50", "Не смогу"]


owm = OWM('c30a0f10eeb9a93501989842cfd6bb23', language = "RU")
cooldown = time.time()-120


@bot.message_handler(commands=['weather'])
def weather(message):
        global cooldown
        GROUP_ID = message.chat.id
        place = owm.weather_at_place('Kyiv')
        wt = place.get_weather()
        if time.time() - cooldown > 120:  
                bot.send_message(GROUP_ID, 'Сегодня '+wt.get_detailed_status()+'\n'+str(round(wt.get_temperature('celsius')['temp']))+"°C🌡")
                cooldown = time.time()
        else:
                bot.delete_message(GROUP_ID, message.message_id)   
        





@bot.message_handler(commands=['sendpoll'])
def start(message):
        global kid 
        global MEMBER_ID 
        global GROUP_ID 
        global MEMBER_RANK
        global timing
        MEMBER_ID = message.from_user.id
        GROUP_ID = message.chat.id
        MEMBER_RANK = bot.get_chat_member(GROUP_ID, MEMBER_ID).status
        global pinpoll 
        pinpoll = message.message_id+2
        if time.time() - timing > 43200:  
                markup = telebot.types.InlineKeyboardMarkup(row_width=3)
                to1 = telebot.types.InlineKeyboardButton(text='Сегодня', callback_data='to1')
                to2 = telebot.types.InlineKeyboardButton(text='Завтра', callback_data='to2')
                to3 = telebot.types.InlineKeyboardButton(text='Послезавтра', callback_data='to3')
                markup.add(to1,to2,to3)
                kid = message.message_id+1
                bot.send_message(chat_id=message.chat.id, text='Когда пойдем на волейбол?', reply_markup=markup)
                timing = time.time()
        else:
                bot.delete_message(GROUP_ID, message.message_id)      

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
        if call.data == 'to1':
                bot.answer_callback_query(callback_query_id=call.id, text='Создан опрос на сегодня')
                bot.delete_message(GROUP_ID, kid)
                volley_to1()
        if call.data == 'to2':
                bot.answer_callback_query(callback_query_id=call.id, text='Создан опрос на завтра')
                bot.delete_message(GROUP_ID, kid)
                volley_to2()
        if call.data == 'to3':
                bot.answer_callback_query(callback_query_id=call.id, text='Создан опрос на послезавтра')
                bot.delete_message(GROUP_ID, kid)
                volley_to3()


def volley_to1():
        global timing
        rtoday()
        if MEMBER_RANK=="creator" or MEMBER_RANK=="administrator":
                bot.send_poll(chat_id=GROUP_ID, question=question_today, options = options, is_anonymous=False) 
                bot.send_message(GROUP_ID, 'Сегодня '+wt.get_detailed_status()+'\n'+str(round(wt.get_temperature('celsius')['temp']))+"°C🌡")
                bot.pin_chat_message(GROUP_ID, pinpoll)
                
def rtoday(): 
        date_today=datetime.date.today() + datetime.timedelta(days=0) 
        global question_today
        question_today = "Волейбол сегодня "+str(date_today.day)+"."+str(date_today.strftime("%m"))+" ("+date_today.strftime("%A")+")?"
        global wt
        place = owm.weather_at_place('Kyiv')
        wt = place.get_weather()

# ----- #     
                
def volley_to2():
        global timing
        rtomorrow()
        if MEMBER_RANK=="creator" or MEMBER_RANK=="administrator":
                bot.send_poll(chat_id=GROUP_ID, question=question_tomorrow, options = options, is_anonymous=False)
                bot.pin_chat_message(GROUP_ID, pinpoll)
def rtomorrow():
        date_tomorrow=datetime.date.today() + datetime.timedelta(days=1) 
        global question_tomorrow
        question_tomorrow = "Волейбол завтра "+str(date_tomorrow.day)+"."+str(date_tomorrow.strftime("%m"))+" ("+date_tomorrow.strftime("%A")+")?"
        

# ----- #  

def volley_to3():
        global timing
        rdayafter()
        if MEMBER_RANK=="creator" or MEMBER_RANK=="administrator":
                bot.send_poll(chat_id=GROUP_ID, question=question_dayafter, options = options, is_anonymous=False)
                bot.pin_chat_message(GROUP_ID, pinpoll)
def rdayafter(): 
        date_dayafter=datetime.date.today() + datetime.timedelta(days=2) 
        global question_dayafter
        question_dayafter = "Волейбол послезавтра "+str(date_dayafter.day)+"."+str(date_dayafter.strftime("%m"))+" ("+date_dayafter.strftime("%A")+")?" 

# ----- #  

@bot.message_handler(commands=['cooldown'])
def send_welcome(message):
        MEMBER_ID = message.from_user.id
        GROUP_ID = message.chat.id
        MEMBER_RANK = bot.get_chat_member(GROUP_ID, MEMBER_ID).status
        global timing 
        global cooldown
        if timing>600: 
                if MEMBER_RANK=="creator":
                        timing=0 
                        cooldown=0
                        bot.send_message(GROUP_ID, 'Куллдауны сброшен')
        else:
                bot.delete_message(GROUP_ID, message.message_id)     


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    user_name = message.new_chat_members[0].first_name
    bot.send_message(message.chat.id, "Добро пожаловать, {0}!".format(user_name))   
        


bot.polling() 
