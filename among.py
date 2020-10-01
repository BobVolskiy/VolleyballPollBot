import telebot
import time 
bot = telebot.TeleBot("1323796504:AAFa8HA_Q4fmhBEuk8C-46FUKr7UsIs5y0s")

cooldown = time.time()-600
@bot.message_handler(commands=['amongus'])
def amongus(message):
        global cooldown
        GROUP_ID = message.chat.id
        name = message.from_user.first_name
        if time.time() - cooldown > 600:  
                bot.send_sticker(GROUP_ID,'CAACAgEAAxkBAAEBZrxfdlrV2gUdNBh_sdOQ9nqOK9wlogACRgADnjOcH9odHIXtfgmvGwQ')
                bot.send_message(GROUP_ID, name+' призывает всех поиграть в Among Us!\n\nЗаходи в голосовой канал, ссылка на игру будет в чате --> https://discord.gg/Z3rKddR')
                cooldown=time.time()  

bot.polling() 
