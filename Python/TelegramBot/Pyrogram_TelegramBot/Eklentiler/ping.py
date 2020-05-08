#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
import datetime

@Client.on_message(Filters.command(['ping'], ['!','.','/']))    # .ping Komutu Kullanıldığı Zaman
def ping(client, message):
    basla = datetime.datetime.now()                             # Zamanı Başlat
    mesaj = message.reply("Bekleyin..")                         # Mesaj'ı Başlatıyoruz
    pong = "Pong!"                                              # Pong'u Başlatıyoruz
    bitir = datetime.datetime.now()                             # Zamanı Durdur
    sure = (bitir - basla).microseconds/10000                   # Duran - Başlayan Zaman
    pong += f"\n\nTepki Süresi : `{sure} ms`"                   # Mesaja Ekle
    mesaj.edit(pong)                                            # Mesajı Düzenle