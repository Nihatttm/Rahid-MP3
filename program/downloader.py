# Copyright (C) 2021 By Veez Music-Project

from __future__ import unicode_literals

import os
import re
import math
import time
import asyncio
import lyricsgenius
from random import randint
from urllib.parse import urlparse

import aiofiles
import aiohttp
import requests
import wget
import yt_dlp
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL

from config import BOT_USERNAME as bn
from driver.decorators import humanbytes
from driver.filters import command, other_filters


ydl_opts = {
    'format': 'best',
    'keepvideo': True,
    'prefer_ffmpeg': False,
    'geo_bypass': True,
    'outtmpl': '%(title)s.%(ext)s',
    'quite': True
}

is_downloading = False


@Client.on_message(command(["bul", f"bul@{bn}"]) & ~filters.edited)
def song(_, message):
    global is_downloading
    query = " ".join(message.command[1:])
    if is_downloading:
        message.reply(
            "» Digər endirmə davam edir, daha sonra yenidən cəhd edin !"
        )
        return
    is_downloading = True
    m = message.reply("🔎 Mahnı axtarılır...")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("❌ Şarkı bulunamadı.\n\nzəhmət olmasa düzgün mahnı adı yazın !")
        print(str(e))
        return
    m.edit("📥 Mahnı yüklənir...")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"• uploader @{bn}"
        host = str(info_dict["uploader"])
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("📤 Mahnı yüklənir ...")
        message.reply_audio(
            audio_file,
            caption=rep,
            performer=host,
            thumb=thumb_name,
            parse_mode="md",
            title=title,
            duration=dur,
        )
        m.delete()
        is_downloading = False
    except Exception as e:
        m.edit("❌ Xəta, bot sahibinin düzəltməsini gözləyin")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


@Client.on_message(
    command(["ara", f"ara@{bn}", "video", f"video@{bn}"]) & ~filters.edited
)
async def vsong(client, message):
    global is_downloading
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    if is_downloading:
        return await message.reply(
            "» Digər endirmə davam edir, daha sonra yenidən cəhd edin !"
        )
    is_downloading = True
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("📥 Video yüklənir...")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 Xəta: `{e}`")
    preview = wget.download(thumbnail)
    await msg.edit("📤 Video yüklənir...")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=ytdl_data["title"],
    )
    is_downloading = False
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)


@Client.on_message(command(["lyrics", f"lyrics@{bn}", "lyrics"]))
async def get_lyric_genius(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**İstifadə edin:**\n\n/lyrics (Mahnı adı)")
    m = await message.reply_text("🔍 Mahnı sözləri axtarılır...")
    query = message.text.split(None, 1)[1]
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("❌ `404` Mahnı sözləri tapılmadı")
    xxx = f"""
**Mahnı:** {query}
**Sənətçi:** {S.artist}
**Mahnı sözü:**
{S.lyrics}"""
    if len(xxx) > 4096:
        await m.delete()
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await message.reply_document(
            document=filename,
            caption=f"**OUTPUT:**\n\n`Lyrics Text`",
            quote=False,
        )
        os.remove(filename)
    else:
        await m.edit(xxx)
