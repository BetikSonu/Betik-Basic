#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from time import time, sleep
from os import listdir

kekikRobot = Client(
    api_id=XXXXXX,                                  # my.telegram.org/apps
    api_hash="XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXX",    # my.telegram.org/apps
    session_name = "@KekikRobot",                   # Fark Etmez
    bot_token = "XXXXX:XXXXXX",
    plugins=dict(root="Eklentiler")
)

adminID = XXXXXXXXXXX

@kekikRobot.on_message(Filters.command(['start'], ['!','.','/']))
def ilk(client, message):
    # Hoş Geldin Mesajı
    message.reply_chat_action("typing")                                 # yazıyor aksiyonu
    message.reply("Hoş Geldin!\n/yardim alabilirsin.")                  # cevapla

    # LOG Alanı
    log = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id}) | Bota Bağlantı Sağladı"
    client.send_message(adminID, log)                                   # adminID'ye log gönder

@kekikRobot.on_message(Filters.command(['yardim'], ['!','.','/']))
def yardim_mesaji(client, message):
    kekik = message.reply("Bekleyin..")
    basla = time()
    kekik.edit("Aranıyor...")                                           # Mesajı Düzenle

    mesaj = f"""Merhaba, [{message.from_user.first_name}](tg://user?id={message.from_user.id})!\n
    Ben @KekikAkademi'de yaratıldım.\n
    Kaynak kodlarım [Burada](https://github.com/KekikRobot)
    Kullanabileceğim komutlar ise eklentilerimde gizli..\n\n"""

    mesaj += "Eklentilerim;\n"                                          # Mesaja Ekle
    for dosya in listdir("./Eklentiler/"):
        if not dosya.endswith(".py"): continue
        mesaj += f"📂 `{dosya.replace('.py','')}`\n"

    bitir = time()
    sure = bitir - basla
    mesaj += f"\nTepki Süresi : `{str(sure)[:4]} sn`"                   # Mesaja Ekle

    try:                                                                # Dene
        kekik.edit(mesaj, disable_web_page_preview=True, parse_mode="Markdown")
    except Exception as hata_mesaji:                                    # Başaramazsan
        kekik.edit(hata_mesaji)                                         # Hatayı Söyle

@kekikRobot.on_message(Filters.command(['eklenti'], ['!','.','/']))
def eklenti_gonder(client, message):
    mesaj = message.reply("Bekleyin..")                         # Mesaj'ı Başlatıyoruz
    girilen_yazi = message.text                                 # komut ile birlikle mesajı tut

    if len(girilen_yazi.split()) == 1:                          # eğer sadece komut varsa
        mesaj.edit("`DosyaAdı` Girmelisin!")                    # uyarı ver
        return                                                  # geri dön

    dosya = " ".join(girilen_yazi.split()[1:2])                 # dosyayı komuttan ayır (birinci kelime)

    if f"{dosya}.py" in listdir("Eklentiler"):
        mesaj.delete()
        message.reply_document(f"./Eklentiler/{dosya}.py")
    else : mesaj.edit('Dosya Bulunamadı!')

if __name__ == '__main__':
    kekikRobot.run()