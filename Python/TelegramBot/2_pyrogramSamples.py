#!/usr/bin/env python
# ! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#---------------------------------------# 
from pyrogram import Client, Filters    #
from time import sleep                  #
#---------------------------------------#

# / Telegram Bağlantısı -------------------------------------------------#
app = Client(
    api_id=XXXXXXXX,                                # my.telegram.org/apps
    api_hash="XXXXXXXX",                            # my.telegram.org/apps
    session_name = "XXXXXXXXX",                     # Fark Etmez
    bot_token = "XXXXXXX:XXXXXXXX"                  # @BotFather
)

adminID = -XXXXXXXXXXX                              # Grup ID
# / Telegram Bağlantısı -------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------#
@app.on_message(Filters.command(['start'], ['!','.','/']))
def ilk(client, message):
    # Hoş Geldin Mesajı
    message.reply_chat_action("typing")             # https://docs.pyrogram.org/api/bound-methods/Message.reply_chat_action
    message.reply("Botumuza Hoş Geldin")

    # LOG Alanı
    log = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | Bota Bağlantı Sağladı"
    client.send_message(adminID, log)
#----------------------------------------------------------------------------------------------------------------------#

@app.on_message(Filters.command(['yardim'], ['!','.','/']))     # ! . / yardim komutunu aldığımda
def komutDeneme(client, message):
    message.reply_chat_action("typing")                         # Yazıyor Gönderiyor Aksiyonu
    message.reply_text("Komut Aldım!", quote=True)  # https://docs.pyrogram.org/api/bound-methods/Message.reply_text
    sleep(1)
    sa = message.reply_text("Selamın Aleyküm Mükerremin Abi")
    sleep(5)
    sa.edit("aleyküm selam desene piç")

    # Dosya Gönder
    message.reply_chat_action("upload_document")                # Fotoğraf Gönderiyor Aksiyonu
    dosya = "DocTest_KekikAkademi.txt"
    message.reply_document(dosya)

    # Foto Gönder
    message.reply_chat_action("upload_photo")                   # Dosya Gönderiyor Aksiyonu
    foto = "FotoTest_KekikAkademi.png"
    message.reply_photo(foto)

@app.on_message(Filters.regex('kim'))                           # cümle içinde eşleşme bulduğunda
def kimsin(client, message):
    message.reply_chat_action("typing")
    message.reply_text("herkesin içişine kimse karışamaz")

app.run()