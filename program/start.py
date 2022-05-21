import asyncio

from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.veez import user
from driver.filters import command, other_filters
from driver.database.dbchat import add_served_chat, is_served_chat
from driver.database.dbpunish import is_gbanned_user
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, MessageNotModified
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAI8bmKIvgnlJyCrq9HIxSvCZCbm5CEjAAIaEAACpvFxHg-Z648-SCRWJAQ")
    await message.reply_text(
        f"""● **ᴍᴇʀʜᴀʙᴀ {message.from_user.mention()} **\n
● **ᴛᴇʟᴇɢʀᴀᴍ sᴇsʟɪ sᴏʜʙᴇᴛʟᴇʀɪ ᴀʀᴀᴄɪʟɪɢɪʏʟᴀ ɢʀᴜʙʟᴀʀᴅᴀ ᴍᴜᴢɪᴋ ᴅɪɴʟᴇᴍᴇɴɪᴢɪ ᴠᴇ ᴠɪᴅᴇᴏ ɪᴢʟᴇᴍᴇɴɪᴢɪ sᴀɢʟɪʏᴀʙɪʟɪʀɪᴍ . . !**

● **ʜᴇʀʜᴀɴɢɪ ʙɪʀ sᴏʀᴜɴ ɪʟᴇ ᴋᴀʀsɪʟᴀsɪʀsᴀɴɪᴢ ᴅᴇsᴛᴇᴋ ɢʀᴜʙᴜᴍᴜᴢᴀ ʙᴀsᴠᴜʀᴍᴀʏɪ ɪʜᴍᴀʟ ᴇᴛᴍᴇʏɪɴ . . !**

● **📚 ᴋᴏᴍᴜᴛʟᴀʀ ʙᴜᴛᴏɴᴜɴᴀ ᴛɪᴋʟᴀʏɪᴘ ᴛᴜᴍ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴏɢʀᴇɴɪɴ . . !**
""",
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
                    InlineKeyboardButton("💝 sᴀʜɪʙɪᴍ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "🗯️ ᴅᴇsᴛᴇᴋ ɢʀᴜʙᴜ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 ʙɪʟɢɪ ᴋᴀɴᴀʟɪ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(c: Client, message: Message):
    chat_id = message.chat.id
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📣 ᴅᴇsᴛᴇᴋ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "🗯️ ʙɪʟɢɪ", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**• ᴍᴇʀʜᴀʙᴀ {message.from_user.mention()} {BOT_NAME}**\n\n🧑🏼‍💻 sᴀʜɪʙɪᴍ: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n👾 ʙᴏᴛ ᴠᴇʀsɪᴏɴ: `v{__version__}`\n🔥 ᴘʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ: `{pyrover}`\n🐍 ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: `{__python_version__}`\n✨ PʏTɢCᴀʟʟs ᴠᴇʀsɪᴏɴ: `{pytover.__version__}`\n🆙 ᴄᴀʟɪsᴍᴀ ᴅᴜʀᴜᴍᴜ: `{uptime}`\n\n❤ **Bᴇɴɪ ɢʀᴜʙᴀ ᴀʟᴅɪɢɪɴɪᴢ ɪᴄɪɴ ᴛᴇsᴇᴋᴋᴜʀʟᴇʀ . . !**"

    await c.send_photo(
        chat_id,
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `ᴘɪɴɢ!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 ʙᴏᴛ ᴅᴜʀᴜᴍᴜ :\n"
        f"• ** ᴜᴘᴛɪᴍᴇ :** `{uptime}`\n"
        f"• ** ᴛɪᴍᴇ :** `{START_TIME_ISO}`"
    )


@Client.on_chat_join_request()
async def approve_join_chat(c: Client, m: ChatJoinRequest):
    if not m.from_user:
        return
    try:
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)
    except FloodWait as e:
        await asyncio.sleep(e.x + 2)
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "**❤️ ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇᴅɪɢɪɴɪᴢ ɪᴄɪɴ ᴛᴇsᴇᴋᴋᴜʀʟᴇʀ . . ! !**\n\n"
                "**Bᴇɴɪ ɢʀᴜʙᴛᴀ ʏᴏɴᴇᴛɪᴄɪ ʏᴀᴘɪɴ ᴠᴇ ᴀʀᴅɪɴᴅᴀɴ /katil ᴋᴏᴍᴜᴛᴜʏʟᴀ ᴀsɪsᴛᴀɴɪ ɢʀᴜʙᴀ ᴅᴀᴠᴇᴛ ᴇᴅɪɴ . . !\n\n**"
                "**Tᴜᴍ ʙᴜɴʟᴀʀɪ ʏᴀᴘᴛɪᴋᴛᴀɴ sᴏɴʀᴀ /reload ᴋᴏᴍᴜᴛᴜɴᴜ ᴋᴜʟʟᴀɴɪɴ ᴠᴇ ʜᴇʀsᴇʏ ʜᴀᴢɪʀ ! ʙᴏᴛᴜ ᴋᴜʟʟᴀɴᴍᴀʏᴀ ʙᴀsʟɪʏᴀʙɪʟɪʀsɪɴɪᴢ . . .**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📣 ʙɪʟɢɪ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("🗯️ ᴅᴇsᴛᴇᴋ", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton("🎙 ᴀsɪssᴛᴀɴ", url=f"https://t.me/{ASSISTANT_NAME}")
                        ]
                    ]
                )
            )


chat_watcher_group = 5

@Client.on_message(group=chat_watcher_group)
async def chat_watcher_func(_, message: Message):
    try:
        userid = message.from_user.id
    except Exception:
        return
    suspect = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if await is_gbanned_user(userid):
        try:
            await message.chat.ban_member(userid)
        except Exception:
            return
        await message.reply_text(
            f"👮🏼 (> {suspect} <)\n\n**Gbanned** user detected, that user has been gbanned by sudo user and was blocked from this Chat !\n\n🚫 **Reason:** potential spammer and abuser."
        )
