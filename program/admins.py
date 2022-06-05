from cache.admins import admins
from driver.veez import call_py, bot
from pyrogram import Client, filters
from driver.design.thumbnail import thumb
from driver.design.chatname import CHAT_TITLE
from driver.queues import QUEUE, clear_queue
from driver.filters import command, other_filters
from driver.decorators import authorized_users_only
from driver.utils import skip_current_song, skip_item
from program.utils.inline import (
    stream_markup,
    close_mark,
    back_mark,
)
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_5, UPDATES_CHANNEL
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        "✅ **Bot yenidən başladıldı!**\n✅ **Admin siyahısı yeniləndi!**"
    )


@Client.on_message(command(["skip", "atla", f"atla@{BOT_USERNAME}", "vatla"]) & other_filters)
@authorized_users_only
async def skip(c: Client, m: Message):
    await m.delete()
    user_id = m.from_user.id
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await c.send_message(chat_id, "**indi heç nə oxunmur!**")
        elif op == 1:
            await c.send_message(chat_id, "» **Növbəti mahnı yoxdur .**\n**Mən səsli çatı tərk edirəm.**")
        elif op == 2:
            await c.send_message(chat_id,  "**Botu**\n**• Səsli söhbətdən ayrılıram.**")
        else:
            buttons = stream_markup(user_id)
            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
            thumbnail = f"{IMG_5}"
            title = f"{op[0]}"
            userid = m.from_user.id
            gcname = m.chat.title
            ctitle = await CHAT_TITLE(gcname)
            image = await thumb(thumbnail, title, userid, ctitle)
            await c.send_photo(
                chat_id,
                photo=image,
                reply_markup=InlineKeyboardMarkup(buttons),
                caption=f"⏭ **Atlandı** Növbəti mahnı.\n\🏷 **Ad:** [{op[0]}]({op[1]})\n💬 **Qrup:** `{chat_id}`\n🎧 **Sorğu:** {requester}",
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **Mahnı növbədən dayandırıldı:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["son", f"son@{BOT_USERNAME}", "end", f"end@{BOT_USERNAME}", "vend"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("✅ Səsli söhbəti tərk edirəm.")
        except Exception as e:
            await m.reply(f"🚫 **Xəta:**\n\n`{e}`")
    else:
        await m.reply("❌ **Heç nə oxunmur**")


@Client.on_message(
    command(["pause", "durdur", f"durdur@{BOT_USERNAME}", "vdurdur"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "⏸ **Trek dayandırıldı .**\n\n• **Davam etmək üçün**\n» /devam yazın."
            )
        except Exception as e:
            await m.reply(f"🚫 **Xəta:**\n\n`{e}`")
    else:
        await m.reply("❌ **Heç bir mahnı oxunmur**")


@Client.on_message(
    command(["resume", "devam", f"devam@{BOT_USERNAME}", "vdevam"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "▶️ **Mahnı davam edildi.**\n\n• **Mahnı dayandırmaq üçün**\n» /durdur yazın."
            )
        except Exception as e:
            await m.reply(f"🚫 **Xəta:**\n\n`{e}`")
    else:
        await m.reply("❌ **Heç bir mahnı oxunmur**")


@Client.on_message(
    command(["mute", f"mute@{BOT_USERNAME}", "vmute"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "🔇 **İstifadəçi botun səsi bağlandı.**\n\n• **Userbot istifadənin səsin açmaq üçün:**\n» /unmute."
            )
        except Exception as e:
            await m.reply(f"🚫 **Xəta:**\n\n`{e}`")
    else:
        await m.reply("❌ **Heç bir mahnı oxunmur**")


@Client.on_message(
    command(["unmute", f"unmute@{BOT_USERNAME}", "vunmute"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "🔊 **İstifadəçi botunun səsi işə salındı.**\n\n• **Userbotun səsini söndürmək üçün**\n» /mute."
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("❌ **Heç bir mahnı oxunmur**")


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Video çatı idarə etmək icazəsi olan admin yalnız bu düyməyə toxuna bilər !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.answer("streaming paused")
            await query.edit_message_text(
                "⏸ Yayım dayandırıldı", reply_markup=back_mark
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀᴏʀ:**\n\n`{e}`", reply_markup=close_mark)
    else:
        await query.answer("❌ Hal-hazırda heçbir səs yayımlanmır", show_alert=True)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Video çatı idarə etmək icazəsi olan admin yalnız bu düyməyə toxuna bilər !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.answer("streaming resumed")
            await query.edit_message_text(
                "▶️ Yayım yenidən başladı", reply_markup=back_mark
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀᴏʀ:**\n\n`{e}`", reply_markup=close_mark)
    else:
        await query.answer("❌ Hal-hazırda heçbir səs yayımlanmır", show_alert=True)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Video çatı idarə etmək icazəsi olan admin yalnız bu düyməyə toxuna bilər!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text("✅ **Bu yayım bitdi*", reply_markup=close_mark)
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀᴏʀ:**\n\n`{e}`", reply_markup=close_mark)
    else:
        await query.answer("❌ Hal-hazırda heçbir səs yayımlanmır", show_alert=True)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Video çatı idarə etmək icazəsi olan admin yalnız bu düyməyə toxuna bilər!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.answer("streaming muted")
            await query.edit_message_text(
                "🔇 userbot uğurla bağlandı", reply_markup=back_mark
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀᴏʀ:**\n\n`{e}`", reply_markup=close_mark)
    else:
        await query.answer("❌ Hal-hazırda heçbir şey yayımlanmır", show_alert=True)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Video çatı idarə etmək icazəsi olan admin yalnız bu düyməyə toxuna bilər!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.answer("streaming unmuted")
            await query.edit_message_text(
                "🔊 userbot uğurla açıldı", reply_markup=back_mark
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ʜᴀᴛᴀ:**\n\n`{e}`", reply_markup=close_mark)
    else:
        await query.answer("❌ Hal-hazırda heçbir şey yayımlanmı", show_alert=True)


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"✅ **Səs səviyyəsi** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"🚫 **Xəta:**\n\n`{e}`")
    else:
        await m.reply("❌ **Yayımda heç nə yoxdur**")
