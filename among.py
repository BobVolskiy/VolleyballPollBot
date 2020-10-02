import telebot
import time 
bot = telebot.TeleBot("1323796504:AAFa8HA_Q4fmhBEuk8C-46FUKr7UsIs5y0s")

cooldown = time.time()-60
@bot.message_handler(commands=['amongus'])
def amongus(message):
        global cooldown
        markdown = """
        *bold text*
        """
        GROUP_ID = message.chat.id
        name = message.from_user.first_name
        if time.time() - cooldown > 60:  
                bot.send_sticker(GROUP_ID,'CAACAgEAAxkBAAEBZrxfdlrV2gUdNBh_sdOQ9nqOK9wlogACRgADnjOcH9odHIXtfgmvGwQ')
                bot.send_message(GROUP_ID, '*'+name+'* призывает в *Among Us*!\n\nЗаходи в голосовой канал, ссылка на игру будет в чате --> https://discord.gg/Z3rKddR',parse_mode= "Markdown")
                cooldown=time.time()  

bot.polling() 
