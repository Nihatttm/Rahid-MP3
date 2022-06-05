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
        f"""● **Salam [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) **\n
● **Mən səsli söhbətlərdə musiqi botuyam 🥰 . . !**

● **Hər hansı problemlə qarşılaşsanız qrupumuza gəlib yaza bilərsiniz . . !**

● **📚 Əmrlər butonuna klikləyib bütün əmrləri öyrənin . . !**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉  Məni qrupa əlavə et  🎉",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton("📚 Əmrlər", callback_data="cbcmds"),
                    InlineKeyboardButton("😍 Sahibim", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "💬 Söhbət Qrup", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "🥰 Kanalım", url=f"https://t.me/{UPDATES_CHANNEL}"
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
        f"""✨ **Salam [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) **

• ** Aşağıdakı butonlara klikləyin . . !

**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 Sahib Əmrləri ", callback_data="cbsudo"),
                    InlineKeyboardButton("📚 Əsas əmrlər", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙  Geri  🔙", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""📚 **Əsas əmrlər :

» /bul => Musiqi yüklə .
» /ara => Video yüklə .
» /oynat => Musiqi oynat .
» /izlet => Video oynat .

» /durdur => Musiqi dayandır .
» /devam => Musiqi davam et .
» /atla => Musiqi keçin .
» /son => Musiqi dayandır .
» /lyrics => Mahnı sözlərini tap .
» /reload => Admin siyahısı yenilə .
» /katil => Asistanı qrupa dəvət et .

» /voynat ( Link ) => Radio və Film kimi canlı asistanı oynat.

» /playlist => Musiqi playlistə əlavə et.

» /list => Sonrakı musiqi siyahını öyrən .

Məlumat : Azərbaycan tərcüməsi əlavə olunub 🥰 . . .

**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  Geri  🔙", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""📚 **Əsas əmrlər :

» /bul => Musiqi yüklə .
» /ara => Video yüklə .
» /oynat => Musiqi oynat .
» /izlet => Video oynat .

» /durdur => Musiqi dayandır .
» /devam => Musiqi davam et .
» /atla => Musiqi keçin .
» /son => Musiqi dayandır .
» /lyrics => Mahnı sözlərini tap .
» /reload => Admin siyahısı yenilə .
» /katil => Asistanı qrupa dəvət et .

» /voynat ( Link ) => Radio və Film kimi canlı asistanı oynat.

» /playlist => Musiqi playlistə əlavə et.

» /list => Sonrakı musiqi siyahını öyrən .

Məlumat : Azərbaycan tərcüməsi əlavə olunub 🥰 . . .

**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""📚 **Sahib əmrləri :

ɴᴏᴛ : Sadəcə
ʙᴏᴛ Sahibi istifadə edə bilər . . .

» /broadcast =>  Yayım etmək !
» /gban => İstifadəçi qadağan etmək !
» /ungban => İstifadəçi qadağanı qaldırmaq !
» /info => Bot məlumatlarını öyrən !
» /restart => Botu yenidən başlat !
» /update => Botu yenilə !
» /hiz => Botun sürətini öyrən !
» /ping => Botun pingi göstərir . . .
» /uptime => Canlı məlumatları göstərir . . .
» /alive => Botun işləmək məlumatını göstərir . . .

**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙  Geri  🔙", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Səsli söhbəti idarə etmək icazəsi olan admin yalnız bu düyməyə toxuna bilər !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **Settings of** {chat}\n\n⏸ : akışı duraklat\n▶️ : akışı devam ettir\n🔇 : asistanı sessize al\n🔊 : asistanın sesini aç\n⏹ : akışı durdur",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("❌ Hazırda heç nə yayımlanmır", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Səsli söhbəti idarə etmək icazəsi olan admin yalnız bu düyməyə toxuna bilər !", show_alert=True)
    await query.message.delete()
