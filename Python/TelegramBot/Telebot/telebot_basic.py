# pip3 install telebot
# pip3 install pyTelegramBotAPI

import telebot,sys

bot = telebot.TeleBot("TOKEN") # Token girilir


@bot.message_handler(["start"]) # /start 'ı yakalarsa :
def start(mesaj): # buradaki def'den devam
    bot.reply_to(mesaj,"Merhaba , start alındı !") # Gelen mesajı yanıtlamak için
    print(mesaj) # mesajı ekrana yazıp bilgileri alabiliriz | log
    print(mesaj.chat.id) # Gelen mesajın hangi chatden geldiğini böyle almış olduk


@bot.message_handler(["ses","muzik"]) # /ses yada /
def ses(mesaj):
    bot.send_audio(mesaj.chat.id,open("mp3.mp3","rb")) # mesaj.chat.id ile müziğin gideceği chat , open() ile de müzik


@bot.message_handler(["mesaj"])
def mesj(mesaj):
    text = mesaj.text # ile mesajın tam text halini alırız . mesela /mesaj ben mesajım 'ın çıktısı /mesaj ben mesajım olur
    if len(text.split()) > 1:
        bot.send_message(mesaj.chat.id," ".join(text.split()[1:]))



@bot.message_handler(["stop"])
def dur(mesaj):
    bot.stop_polling()

# Basit telebot örneği .




bot.polling() # Botun çalışması için
print("Polling bitti .")


# Token olmadığı için test edilmedi . Hata varsa github'dan düzeltin lütfen .