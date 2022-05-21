# Copyright (C) 2021 By Veez Music-Project
# Commit Start Date 20/10/2021
# Finished On 28/10/2021

import re
import asyncio

from config import BOT_USERNAME, IMG_1, IMG_2, IMG_5
from program.utils.inline import stream_markup
from driver.design.thumbnail import thumb
from driver.design.chatname import CHAT_TITLE
from driver.filters import command, other_filters
from driver.queues import QUEUE, add_to_queue
from driver.veez import call_py, user
from pyrogram import Client
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)
from youtubesearchpython import VideosSearch


def ytsearch(query: str):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        return [songname, url, duration, thumbnail]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "best[height<=?720][width<=?1280]",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@Client.on_message(command(["izlet", f"izlet@{BOT_USERNAME}"]) & other_filters)
async def vplay(c: Client, m: Message):
    await m.delete()
    replied = m.reply_to_message
    chat_id = m.chat.id
    user_id = m.from_user.id
    if m.sender_chat:
        return await m.reply_text(
            "sen bir __Anonim__ kullanıcısısın !\n\n» bu botu kullanmak için gerçek kullanıcı hesabınıza geri dönün."
        )
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"error:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"● ʙᴇɴɪ ᴋᴜʟʟᴀɴᴍᴀᴋ ɪᴄɪɴ ᴀssᴀɢɪᴅᴀᴋɪ ʏᴇᴛᴋɪʟᴇʀɪ ᴠᴇʀᴍᴇɴɪᴢ ɢᴇʀᴇᴋɪʀ . . ! **ɪᴢɪɴʟᴇʀ**:\n\n» ᴍᴇsᴀᴊʟᴀʀɪ sɪʟᴍᴇ \n» ʙᴀɢʟᴀɴᴛɪ ɪʟᴇ ᴅᴀᴠᴇᴛ ᴇᴛᴍᴇ\n» sᴇsʟɪ sᴏʜʙᴇᴛʟᴇʀɪ ʏᴏɴᴇᴛᴍᴇ\n\nʙɪᴛᴛɪɢɪɴᴅᴇ /reload ʏᴀᴢɪɴ . . !"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "💡 ʙᴇɴɪ ᴋᴜʟʟᴀɴᴍᴀᴋ ɪᴄɪɴ ᴀssᴀɢɪᴅᴀᴋɪ ʏᴇᴛᴋɪʟᴇʀɪ ᴠᴇʀᴍᴇɴɪᴢ ɢᴇʀᴇᴋɪʀ :"
            + "\n\n» sᴇsʟɪ sᴏʜʙᴇᴛʟᴇʀɪ ʏᴏɴᴇᴛᴍᴇ "
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "💡 ʙᴇɴɪ ᴋᴜʟʟᴀɴᴍᴀᴋ ɪᴄɪɴ ᴀssᴀɢɪᴅᴀᴋɪ ʏᴇᴛᴋɪʟᴇʀɪ ᴠᴇʀᴍᴇɴɪᴢ ɢᴇʀᴇᴋɪʀ :"
            + "\n\n» ᴍᴇsᴀᴊʟᴀʀɪ sɪʟᴍᴇ "
        )
        return
    if not a.can_invite_users:
        await m.reply_text(
            "💡 ʙᴇɴɪ ᴋᴜʟʟᴀɴᴍᴀᴋ ɪᴄɪɴ ᴀssᴀɢɪᴅᴀᴋɪ ʏᴇᴛᴋɪʟᴇʀɪ ᴠᴇʀᴍᴇɴɪᴢ ɢᴇʀᴇᴋɪʀ :"
            + "\n\n» ʙᴀɢʟᴀɴᴛɪ ɪʟᴇ ᴅᴀᴠᴇᴛ ᴇᴛᴍᴇ "
        )
        return
    try:
        ubot = (await user.get_me()).id
        b = await c.get_chat_member(chat_id, ubot) 
        if b.status == "kicked":
            await c.unban_chat_member(chat_id, ubot)
            invitelink = await c.export_chat_invite_link(chat_id)
            if invitelink.startswith("https://t.me/+"):
                invitelink = invitelink.replace(
                    "https://t.me/+", "https://t.me/joinchat/"
                )
            await user.join_chat(invitelink)
    except UserNotParticipant:
        try:
            invitelink = await c.export_chat_invite_link(chat_id)
            if invitelink.startswith("https://t.me/+"):
                invitelink = invitelink.replace(
                    "https://t.me/+", "https://t.me/joinchat/"
                )
            await user.join_chat(invitelink)
        except UserAlreadyParticipant:
            pass
        except Exception as e:
            return await m.reply_text(
                f"❌ **ᴀsɪsᴛᴀɴ ᴋᴀᴛɪʟᴀᴍᴀᴅɪ**\n\n**reason**: `{e}`"
            )

    if replied:
        if replied.video or replied.document:
            loser = await replied.reply("📥 **ᴠɪᴅᴇᴏ ɪɴᴅɪʀɪʟɪʏᴏʀ...**")
            dl = await replied.download()
            link = replied.link
            if len(m.command) < 2:
                Q = 720
            else:
                pq = m.text.split(None, 1)[1]
                if pq == "720" or "480" or "360":
                    Q = int(pq)
                else:
                    Q = 720
                    await loser.edit(
                        "» ʏᴀʟɴɪᴢᴄᴀ 360ᴘ , 480ᴘ , 720ᴘ ᴏʏɴᴀᴛɪʟᴀʙɪʟɪʀ \n💡 **sɪᴍᴅɪ 720p'ᴅᴇ ᴠɪᴅᴇᴏ ᴀᴋɪsɪ**"
                    )
            try:
                if replied.video:
                    songname = replied.video.file_name[:70]
                    duration = replied.video.duration
                elif replied.document:
                    songname = replied.document.file_name[:70]
                    duration = replied.document.duration
            except BaseException:
                songname = "Video"

            if chat_id in QUEUE:
                gcname = m.chat.title
                ctitle = await CHAT_TITLE(gcname)
                title = songname
                userid = m.from_user.id
                thumbnail = f"{IMG_5}"
                image = await thumb(thumbnail, title, userid, ctitle)
                pos = add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await loser.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                buttons = stream_markup(user_id)
                await m.reply_photo(
                    photo=image,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"⏩ **ᴘᴀʀᴄᴀ sɪʀᴀʏᴀ ᴇᴋʟᴇɴᴅɪ »** `{pos}`\n\n📝 **ɪsɪᴍ:** [{songname}]({link}) | `video`\n⌚ **sᴜʀᴇ:** `{duration}`\n📒 **ᴛᴀʟᴇᴘ:** {requester}",
                )
            else:
                gcname = m.chat.title
                ctitle = await CHAT_TITLE(gcname)
                title = songname
                userid = m.from_user.id
                thumbnail = f"{IMG_5}"
                image = await thumb(thumbnail, title, userid, ctitle)
                if Q == 720:
                    amaze = HighQualityVideo()
                elif Q == 480:
                    amaze = MediumQualityVideo()
                elif Q == 360:
                    amaze = LowQualityVideo()
                await loser.edit("🔄 **ʏᴜᴋʟᴇɴɪʏᴏʀ ...**")
                await call_py.join_group_call(
                    chat_id,
                    AudioVideoPiped(
                        dl,
                        HighQualityAudio(),
                        amaze,
                    ),
                    stream_type=StreamType().local_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await loser.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                buttons = stream_markup(user_id)
                await m.reply_photo(
                    photo=image,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"🏷 **ɪsɪᴍ:** [{songname}]({link}) | `video`\n⌚ **sᴜʀᴇ:** `{duration}`\n🎧 **ᴛᴀʟᴇᴘ:** {requester}",
                )
        else:
            if len(m.command) < 2:
                await m.reply(
                    "» ᴠɪᴅᴇᴏ ᴅᴏsʏᴀsɪɴᴀ ʏᴀɴɪᴛ ᴠᴇʀɪɴ ᴠᴇʏᴀ ᴠɪᴅᴇᴏ ɪsᴍɪ ᴠᴇʀɪɴ .**"
                )
            else:
                loser = await c.send_message(chat_id, "🔍 **ᴀʀᴀɴɪʏᴏʀ ...**")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                Q = 720
                amaze = HighQualityVideo()
                if search == 0:
                    await loser.edit("❌ **sᴏɴᴜᴄ ʙᴜʟᴜɴᴀᴍᴀᴅɪ .**")
                else:
                    songname = search[0]
                    title = search[0]
                    url = search[1]
                    duration = search[2]
                    thumbnail = search[3]
                    userid = m.from_user.id
                    gcname = m.chat.title
                    ctitle = await CHAT_TITLE(gcname)
                    image = await thumb(thumbnail, title, userid, ctitle)
                    veez, ytlink = await ytdl(url)
                    if veez == 0:
                        await loser.edit(f"❌ yt-dl sorunları algılandı\n\n» `{ytlink}`")
                    else:
                        if chat_id in QUEUE:
                            pos = add_to_queue(
                                chat_id, songname, ytlink, url, "Video", Q
                            )
                            await loser.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            buttons = stream_markup(user_id)
                            await m.reply_photo(
                                photo=image,
                                reply_markup=InlineKeyboardMarkup(buttons),
                                caption=f"⏩ **ᴘᴀʀᴄᴀ sɪʀᴀʏᴀ ᴇᴋʟᴇɴᴅɪ »** `{pos}`\n\n📝 **ɪsɪᴍ:** [{songname}]({url}) | `video`\n⌚ **sᴜʀᴇ:** `{duration}`\n📒 **ᴛᴀʟᴇᴘ:** {requester}",
                            )
                        else:
                            try:
                                await loser.edit("🔄 **ʏᴜᴋʟᴇɴɪʏᴏʀ ...**")
                                await call_py.join_group_call(
                                    chat_id,
                                    AudioVideoPiped(
                                        ytlink,
                                        HighQualityAudio(),
                                        amaze,
                                    ),
                                    stream_type=StreamType().local_stream,
                                )
                                add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                                await loser.delete()
                                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                                buttons = stream_markup(user_id)
                                await m.reply_photo(
                                    photo=image,
                                    reply_markup=InlineKeyboardMarkup(buttons),
                                    caption=f"🏷 **ɪsɪᴍ:** [{songname}]({url}) | `video`\n⌚ **sᴜʀᴇ:** `{duration}`\n🎧 **ᴛᴀʟᴇᴘ:** {requester}",
                                )
                            except Exception as ep:
                                await loser.delete()
                                await m.reply_text(f"🚫 error: `{ep}`")

    else:
        if len(m.command) < 2:
            await m.reply(
                "» ᴠɪᴅᴇᴏ ᴅᴏsʏᴀsɪɴᴀ ʏᴀɴɪᴛ ᴠᴇʀɪɴ ᴠᴇʏᴀ ᴠɪᴅᴇᴏ ɪsᴍɪ ᴠᴇʀɪɴ .**"
            )
        else:
            loser = await c.send_message(chat_id, "🔍 **ᴀʀᴀɴɪʏᴏʀ ...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            Q = 720
            amaze = HighQualityVideo()
            if search == 0:
                await loser.edit("❌ **sᴏɴᴜᴄ ʙᴜʟᴜɴᴀᴍᴀᴅɪ.**")
            else:
                songname = search[0]
                title = search[0]
                url = search[1]
                duration = search[2]
                thumbnail = search[3]
                userid = m.from_user.id
                gcname = m.chat.title
                ctitle = await CHAT_TITLE(gcname)
                image = await thumb(thumbnail, title, userid, ctitle)
                veez, ytlink = await ytdl(url)
                if veez == 0:
                    await loser.edit(f"❌ yt-dl sorunları algılandı\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                        await loser.delete()
                        requester = (
                            f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                        )
                        buttons = stream_markup(user_id)
                        await m.reply_photo(
                            photo=image,
                            reply_markup=InlineKeyboardMarkup(buttons),
                            caption=f"⏩ **ᴘᴀʀᴄᴀ sɪʀᴀʏᴀ ᴇᴋʟᴇɴᴅɪ »** `{pos}`\n\n📝 **ɪsɪᴍ:** [{songname}]({url}) | `video`\n⌚ **sᴜʀᴇ:** `{duration}`\n📒 **ᴛᴀʟᴇᴘ:** {requester}",
                        )
                    else:
                        try:
                            await loser.edit("🔄 **ʏᴜᴋʟᴇɴɪʏᴏʀ ...**")
                            await call_py.join_group_call(
                                chat_id,
                                AudioVideoPiped(
                                    ytlink,
                                    HighQualityAudio(),
                                    amaze,
                                ),
                                stream_type=StreamType().local_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                            await loser.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            buttons = stream_markup(user_id)
                            await m.reply_photo(
                                photo=image,
                                reply_markup=InlineKeyboardMarkup(buttons),
                                caption=f"🏷 **ɪsɪᴍ:** [{songname}]({url}) | `video`\n⌚ **sᴜʀᴇ:** `{duration}`\n🎧 **ᴛᴀʟᴇᴘ:** {requester}",
                            )
                        except Exception as ep:
                            await loser.delete()
                            await m.reply_text(f"🚫 error: `{ep}`")


@Client.on_message(command(["voynat", "vplay", f"voynat@{BOT_USERNAME}"]) & other_filters)
async def vstream(c: Client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    user_id = m.from_user.id
    if m.sender_chat:
        return await m.reply_text(
            "sen bir __Anonim__ kullanıcısısın !\n\n» bu botu kullanmak için gerçek kullanıcı hesabınıza geri dönün."
        )
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"error:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"● ʙᴇɴɪ ᴋᴜʟʟᴀɴᴍᴀᴋ ɪᴄɪɴ ᴀssᴀɢɪᴅᴀᴋɪ ʏᴇᴛᴋɪʟᴇʀɪ ᴠᴇʀᴍᴇɴɪᴢ ɢᴇʀᴇᴋɪʀ . . ! **ɪᴢɪɴʟᴇʀ**:\n\n» ᴍᴇsᴀᴊʟᴀʀɪ sɪʟᴍᴇ \n» ʙᴀɢʟᴀɴᴛɪ ɪʟᴇ ᴅᴀᴠᴇᴛ ᴇᴛᴍᴇ\n» sᴇsʟɪ sᴏʜʙᴇᴛʟᴇʀɪ ʏᴏɴᴇᴛᴍᴇ\n\nʙɪᴛᴛɪɢɪɴᴅᴇ /reload ʏᴀᴢɪɴ . . !"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "💡 ʙᴇɴɪ ᴋᴜʟʟᴀɴᴍᴀᴋ ɪᴄɪɴ ᴀssᴀɢɪᴅᴀᴋɪ ʏᴇᴛᴋɪʟᴇʀɪ ᴠᴇʀᴍᴇɴɪᴢ ɢᴇʀᴇᴋɪʀ :"
            + "\n\n» sᴇsʟɪ sᴏʜʙᴇᴛʟᴇʀɪ ʏᴏɴᴇᴛᴍᴇ "
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "💡 ʙᴇɴɪ ᴋᴜʟʟᴀɴᴍᴀᴋ ɪᴄɪɴ ᴀssᴀɢɪᴅᴀᴋɪ ʏᴇᴛᴋɪʟᴇʀɪ ᴠᴇʀᴍᴇɴɪᴢ ɢᴇʀᴇᴋɪʀ :"
            + "\n\n» ᴍᴇsᴀᴊʟᴀʀɪ sɪʟᴍᴇ "
        )
        return
    if not a.can_invite_users:
        await m.reply_text(
            "💡 ʙᴇɴɪ ᴋᴜʟʟᴀɴᴍᴀᴋ ɪᴄɪɴ ᴀssᴀɢɪᴅᴀᴋɪ ʏᴇᴛᴋɪʟᴇʀɪ ᴠᴇʀᴍᴇɴɪᴢ ɢᴇʀᴇᴋɪʀ :"
            + "\n\n» ʙᴀɢʟᴀɴᴛɪ ɪʟᴇ ᴅᴀᴠᴇᴛ ᴇᴛᴍᴇ"
        )
        return
    try:
        ubot = (await user.get_me()).id
        b = await c.get_chat_member(chat_id, ubot)
        if b.status == "kicked":
            await c.unban_chat_member(chat_id, ubot)
            invitelink = await c.export_chat_invite_link(chat_id)
            if invitelink.startswith("https://t.me/+"):
                invitelink = invitelink.replace(
                    "https://t.me/+", "https://t.me/joinchat/"
                )
            await user.join_chat(invitelink)
    except UserNotParticipant:
        try:
            invitelink = await c.export_chat_invite_link(chat_id)
            if invitelink.startswith("https://t.me/+"):
                invitelink = invitelink.replace(
                    "https://t.me/+", "https://t.me/joinchat/"
                )
            await user.join_chat(invitelink)
        except UserAlreadyParticipant:
            pass
        except Exception as e:
            return await m.reply_text(
                f"❌ **ᴀsɪsᴛᴀɴ ᴋᴀᴛɪʟᴀᴍᴀᴅɪ**\n\n**reason**: `{e}`"
            )

    if len(m.command) < 2:
        await m.reply("**» akış için bana bir canlı youtube bağlantısı verin.**")
    else:
        if len(m.command) == 2:
            link = m.text.split(None, 1)[1]
            Q = 720
            loser = await c.send_message(chat_id, "**ᴄᴀɴʟɪ ᴠɪᴅᴇᴏ ᴀᴋɪsɪ...**")
        elif len(m.command) == 3:
            op = m.text.split(None, 1)[1]
            link = op.split(None, 1)[0]
            quality = op.split(None, 1)[1]
            if quality == "720" or "480" or "360":
                Q = int(quality)
            else:
                Q = 720
                await m.reply(
                    "» ʏᴀʟɴɪᴢᴄᴀ 360ᴘ , 480ᴘ , 720ᴘ ᴏʏɴᴀᴛɪʟᴀʙɪʟɪʀ \n💡 **sɪᴍᴅɪ 720p'ᴅᴇ ᴠɪᴅᴇᴏ ᴀᴋɪsɪ**"
                )
            loser = await c.send_message(chat_id, "**ᴄᴀɴʟɪ ʏᴀʏɪɴ ᴀᴋɪsɪ...**")
        else:
            await m.reply("**/vstream {link} {720/480/360}**")

        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, link)
        if match:
            veez, livelink = await ytdl(link)
        else:
            livelink = link
            veez = 1

        if veez == 0:
            await loser.edit(f"❌ yt-dl sorunları algılandı\n\n» `{livelink}`")
        else:
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, "ᴄᴀɴʟɪ ʏᴀʏɪɴ", livelink, link, "Video", Q)
                await loser.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                buttons = stream_markup(user_id)
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"⏩ **ᴘᴀʀᴄᴀ sɪʀᴀʏᴀ ᴇᴋʟᴇɴᴅɪ »** `{pos}`\n\n💬 **ɢʀᴜʙ:** `{chat_id}`\n📒 **ᴛᴀʟᴇᴘ:** {requester}",
                )
            else:
                if Q == 720:
                    amaze = HighQualityVideo()
                elif Q == 480:
                    amaze = MediumQualityVideo()
                elif Q == 360:
                    amaze = LowQualityVideo()
                try:
                    await loser.edit("🔄 **ʏᴜᴋʟᴇɴɪʏᴏʀ . . .**")
                    await call_py.join_group_call(
                        chat_id,
                        AudioVideoPiped(
                            livelink,
                            HighQualityAudio(),
                            amaze,
                        ),
                        stream_type=StreamType().live_stream,
                    )
                    add_to_queue(chat_id, "ᴄᴀɴʟɪ ʏᴀʏɪɴ", livelink, link, "Video", Q)
                    await loser.delete()
                    requester = (
                        f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                    )
                    buttons = stream_markup(user_id)
                    await m.reply_photo(
                        photo=f"{IMG_2}",
                        reply_markup=InlineKeyboardMarkup(buttons),
                        caption=f"⏩ **[ᴄᴀɴʟɪ ᴀᴋɪs]({link}) ᴀᴋɪs ʙᴀsʟᴀᴅɪ.**\n\n💬 **ɢʀᴜʙ:** `{chat_id}`\n📒 **ᴛᴀʟᴇᴘ:** {requester}",
                    )
                except Exception as ep:
                    await loser.delete()
                    await m.reply_text(f"🚫 error: `{ep}`")
