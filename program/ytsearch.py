from config import BOT_USERNAME
from driver.filters import command
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch


@Client.on_message(command(["search", f"search@{BOT_USERNAME}"]))
async def ytsearch(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**Mənə videonun adını yazın!**")
    query = message.text.split(None, 1)[1]
    m = await message.reply_text("🔎 **Axtarılır. . .**")
    results = YoutubeSearch(query, max_results=5).to_dict()
    text = ""
    for i in range(5):
        try:
            text += f"🏷 **Ad:** __{results[i]['title']}__\n"
            text += f"⏱ **Müddət:** `{results[i]['duration']}`\n"
            text += f"👀 **Baxış sayı:** `{results[i]['views']}`\n"
            text += f"📣 **Kanal:** {results[i]['channel']}\n"
            text += f"🔗 **Link:** https://www.youtube.com{results[i]['url_suffix']}\n\n"
        except IndexError:
            break
    await m.edit_text(
        text,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🗑 Bağla", callback_data="cls")]]
        ),
    )
