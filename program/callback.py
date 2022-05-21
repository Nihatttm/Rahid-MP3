# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""● **ᴍᴇʀʜᴀʙᴀ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) **\n
● **ᴛᴇʟᴇɢʀᴀᴍ sᴇsʟɪ sᴏʜʙᴇᴛʟᴇʀɪ ᴀʀᴀᴄɪʟɪɢɪʏʟᴀ ɢʀᴜʙʟᴀʀᴅᴀ ᴍᴜᴢɪᴋ ᴅɪɴʟᴇᴍᴇɴɪᴢɪ ᴠᴇ ᴠɪᴅᴇᴏ ɪᴢʟᴇᴍᴇɴɪᴢɪ sᴀɢʟɪʏᴀʙɪʟɪʀɪᴍ . . !**

● **ʜᴇʀʜᴀɴɢɪ ʙɪʀ sᴏʀᴜɴ ɪʟᴇ ᴋᴀʀsɪʟᴀsɪʀsᴀɴɪᴢ ᴅᴇsᴛᴇᴋ ɢʀᴜʙᴜᴍᴜᴢᴀ ʙᴀsᴠᴜʀᴍᴀʏɪ ɪʜᴍᴀʟ ᴇᴛᴍᴇʏɪɴ . . !**

● **📚 ᴋᴏᴍᴜᴛʟᴀʀ ʙᴜᴛᴏɴᴜɴᴀ ᴛɪᴋʟᴀʏɪᴘ ᴛᴜᴍ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴏɢʀᴇɴɪɴ . . !**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉  ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ  🎉",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton("📚 ᴋᴏᴍᴜᴛʟᴀʀ", callback_data="cbcmds"),
                    InlineKeyboardButton("🤠 sᴀʜɪʙɪᴍ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "📝 ᴅᴇsᴛᴇᴋ ɢʀᴜʙᴜ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "🗯️ ʙɪʟɢɪ ᴋᴀɴᴀʟɪ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""❓ How to use this Bot ?, read the Guide below !

1.) First, add this bot to your Group.
2.) Then, promote this bot as administrator on the Group also give all permissions except Anonymous admin.
3.) After promoting this bot, type /reload in Group to update the admin data.
3.) Invite @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her (unfortunately the userbot will joined by itself when you type `/play (song name)` or `/vplay (song name)`).
4.) Turn on/Start the video chat first before start to play video/music.

`- END, EVERYTHING HAS BEEN SETUP -`

📌 If the userbot not joined to video chat, make sure if the video chat already turned on and the userbot in the chat.

💡 If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  Go Back  🔙", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""✨ **ᴍᴇʀʜᴀʙᴀ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) **

• ** ᴀssᴀɢɪᴅᴀᴋɪ ʙᴜᴛᴏɴʟᴀʀᴀ ᴛɪᴋʟᴀʏɪɴ . . !

**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 sᴀʜɪᴘ ᴋᴏᴍᴜᴛʟᴀʀɪ ", callback_data="cbsudo"),
                    InlineKeyboardButton("📚 ᴛᴇᴍᴇʟ ᴋᴏᴍᴜᴛʟᴀʀ", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙  ɢᴇʀɪ ɢɪᴛ  🔙", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""📚 **ᴛᴇᴍᴇʟ ᴋᴏᴍᴜᴛʟᴀʀɪ :

» /bul => ᴍᴜᴢɪᴋ ɪɴᴅɪʀ .
» /ara => ᴠɪᴅᴇᴏ ɪɴᴅɪʀ .
» /oynat => ᴍᴜᴢɪᴋ ᴏʏɴᴀᴛ .
» /izlet => ᴠɪᴅᴇᴏ ᴏʏɴᴀᴛ .

» /durdur => ᴍᴜᴢɪɢɪ ᴅᴜʀᴅᴜʀ .
» /devam => ᴍᴜᴢɪɢɪ sᴜʀᴅᴜʀ .
» /atla => ᴍᴜᴢɪɢɪ ᴀᴛʟᴀ .
» /son => ᴍᴜᴢɪɢɪ sᴏɴʟᴀɴᴅɪʀ .
» /lyrics => sᴀʀᴋɪ sᴏᴢʟᴇʀɪɴɪ ʙᴜʟ .
» /reload => ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪɴɪ ɢᴜɴᴄᴇʟʟᴇʀ .
» /katil => ᴀsɪsᴛᴀɴɪ ɢʀᴜʙᴀ ᴅᴀᴠᴇᴛ ᴇᴅᴇʀ .

» /voynat ( ʟɪɴᴋ ) => ʀᴀᴅɪᴏ ᴠᴇ ғɪʟᴍ ɢɪʙɪ  ᴄᴀɴʟɪ ᴀᴋɪsʟᴀʀɪ ᴏʏɴᴀᴛ.

» /playlist => ᴍᴜᴢɪɢɪ PʟᴀʏLɪsᴛ'ᴇ ᴇᴋʟᴇ.

» /list => sɪʀᴀᴅᴀᴋɪ ᴍᴜᴢɪᴋ ʟɪsᴛᴇsɪɴɪ ᴏɢʀᴇɴ .

ʙɪʟɢɪ : ᴛᴜʀᴋᴄᴇ ᴠᴇ ɪɴɢɪʟɪᴢᴄᴇ ᴋᴏᴍᴜᴛʟᴀʀ ɢᴜɴᴄᴇʟᴅɪʀ ᴋᴇʏғɪɴɪᴢᴇ ɢᴏʀᴇ . . .

**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ɢᴇʀɪ ɢɪᴛ  🔙", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""📚 **ᴛᴇᴍᴇʟ ᴋᴏᴍᴜᴛʟᴀʀɪ :

» /bul => ᴍᴜᴢɪᴋ ɪɴᴅɪʀ .
» /ara => ᴠɪᴅᴇᴏ ɪɴᴅɪʀ .
» /oynat => ᴍᴜᴢɪᴋ ᴏʏɴᴀᴛ .
» /izlet => ᴠɪᴅᴇᴏ ᴏʏɴᴀᴛ .

» /durdur => ᴍᴜᴢɪɢɪ ᴅᴜʀᴅᴜʀ .
» /devam => ᴍᴜᴢɪɢɪ sᴜʀᴅᴜʀ .
» /atla => ᴍᴜᴢɪɢɪ ᴀᴛʟᴀ .
» /son => ᴍᴜᴢɪɢɪ sᴏɴʟᴀɴᴅɪʀ .
» /lyrics => sᴀʀᴋɪ sᴏᴢʟᴇʀɪɴɪ ʙᴜʟ .
» /reload => ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪɴɪ ɢᴜɴᴄᴇʟʟᴇʀ .
» /katil => ᴀsɪsᴛᴀɴɪ ɢʀᴜʙᴀ ᴅᴀᴠᴇᴛ ᴇᴅᴇʀ .

» /voynat ( ʟɪɴᴋ ) => ʀᴀᴅɪᴏ ᴠᴇ ғɪʟᴍ ɢɪʙɪ  ᴄᴀɴʟɪ ᴀᴋɪsʟᴀʀɪ ᴏʏɴᴀᴛ.

» /playlist => ᴍᴜᴢɪɢɪ PʟᴀʏLɪsᴛ'ᴇ ᴇᴋʟᴇ.

» /list => sɪʀᴀᴅᴀᴋɪ ᴍᴜᴢɪᴋ ʟɪsᴛᴇsɪɴɪ ᴏɢʀᴇɴ .

ʙɪʟɢɪ : ᴛᴜʀᴋᴄᴇ ᴠᴇ ɪɴɢɪʟɪᴢᴄᴇ ᴋᴏᴍᴜᴛʟᴀʀ ɢᴜɴᴄᴇʟᴅɪʀ ᴋᴇʏғɪɴɪᴢᴇ ɢᴏʀᴇ . . .

**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 ɢᴇʀɪ ɢɪᴛ", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""📚 **sᴀʜɪᴘ ᴋᴏᴍᴜᴛʟᴀʀɪ :

ɴᴏᴛ : Sᴀᴅᴇᴄᴇ
ʙᴏᴛ sᴀʜɪʙɪ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ . . .

» /broadcast =>  ʏᴀʏɪɴ ʏᴀᴘᴍᴀᴋ !
» /gban => ᴋᴜʀᴇsᴇʟ ʏᴀsᴀᴋʟᴀᴍᴀ !
» /ungban => ᴋᴜʀᴇsᴇʟ ʏᴀsᴀᴋ ᴋᴀʟᴅɪʀᴍᴀ !
» /info => ʙᴏᴛᴜɴ ʙɪʟɢɪʟᴇʀɪɴɪ ᴏɢʀᴇɴ !
» /restart => ʙᴏᴛᴜ ʏᴇɴɪᴅᴇɴ ʙᴀsʟᴀᴛ !
» /update => ʙᴏᴛᴜ ɢᴜɴᴄᴇʟʟᴇ !
» /hiz => ʙᴏᴛᴜɴ ʜɪᴢɪɴɪ ᴏɢʀᴇɴ !
» /ping => ᴘɪɴɢ ᴅᴜʀᴜᴍᴜɴᴜ ɢᴏsᴛᴇʀɪʀ . . .
» /uptime => ᴄᴀɴʟɪ ʙɪʟɢɪʟᴇʀɪ ɢᴏsᴛᴇʀɪʀ . . .
» /alive => ʙᴏᴛᴜɴ ᴄᴀʟɪsᴍᴀ ᴅᴜʀᴜᴍᴜɴᴜ ɢᴏsᴛᴇʀɪʀ . . .

**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  ɢᴇʀɪ ɢɪᴛ  🔙", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **Settings of** {chat}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("❌ şu anda hiçbir şey yayınlanmıyor", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Yalnızca bu düğmeye dokunabilen görüntülü sohbet yönetme iznine sahip yönetici !", show_alert=True)
    await query.message.delete()
