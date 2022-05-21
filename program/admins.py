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
        "✅ Bᴏᴛ **ʏᴇɴɪᴅᴇɴ ʙᴀsʟᴀᴛɪʟᴅɪ !**\n✅ **ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪ ɢᴜɴᴄᴇʟʟᴇɴᴅɪ !**"
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
            await c.send_message(chat_id, "**sᴜ ᴀɴᴅᴀ ʜɪᴄʙɪʀ sᴇʏ ᴄᴀʟᴍɪʏᴏʀ !**")
        elif op == 1:
            await c.send_message(chat_id, "» **sɪʀᴀᴅᴀ ʙᴀsᴋᴀ sᴀʀᴋɪ ʏᴏᴋ .**\n**sᴇsʟɪ sᴏʜʙᴇᴛᴛᴇɴ ᴀʏʀɪʟɪʏᴏʀᴜᴍ .**")
        elif op == 2:
            await c.send_message(chat_id, "🗑️ **sɪʀᴀʏɪ ᴛᴇᴍɪᴢʟᴇᴍᴇ**\n**• ɢᴏʀᴜɴᴛᴜʟᴜ sᴏʜʙᴇᴛᴛᴇɴ ᴀʏʀɪʟɪʏᴏʀᴜᴍ.**")
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
                caption=f"⏭ **ᴀᴛʟᴀɴᴅɪ** sᴏɴʀᴀᴋɪ ᴘᴀʀᴄᴀ .\n\n📝 **ɪsɪᴍ:** [{op[0]}]({op[1]})\n💬 **ɢʀᴜʙ:** `{chat_id}`\n📒 **ᴛᴀʟᴇᴘ:** {requester}",
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **sᴀʀᴋɪ ᴋᴜʏʀᴜᴋᴛᴀɴ ᴋᴀʟᴅɪʀɪʟᴅɪ:**"
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
            await m.reply("✅ sᴇsʟɪ sᴏʜʙᴇᴛᴛᴇɴ ᴀʏʀɪʟɪʏᴏʀᴜᴍ .")
        except Exception as e:
            await m.reply(f"🚫 **ʜᴀᴛᴀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ʜɪᴄʙɪʀ sᴇʏ ᴄᴀʟᴍɪʏᴏʀ**")


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
                "⏸ **ᴘᴀʀᴄᴀ ᴅᴜʀᴅᴜʀᴜʟᴅᴜ .**\n\n• **sᴜʀᴅᴜʀᴍᴇᴋ ɪᴄɪɴ **\n» /devam ʏᴀᴢɪɴ ."
            )
        except Exception as e:
            await m.reply(f"🚫 **ʜᴀᴛᴀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ʜɪᴄʙɪʀ sᴇʏ ᴄᴀʟᴍɪʏᴏʀ**")


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
                "▶️ **ᴘᴀʀᴄᴀ ᴅᴇᴠᴀᴍ ᴇᴛɪʀɪʟᴅɪ .**\n\n• **ᴅᴜʀᴅᴜʀᴍᴀᴋ ɪᴄɪɴ**\n» /durdur ʏᴀᴢɪɴ ."
            )
        except Exception as e:
            await m.reply(f"🚫 **ʜᴀᴛᴀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ʜɪᴄ ʙɪʀ sᴇʏ ᴄᴀʟᴍɪʏᴏʀ**")


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
                "🔇 **Kullanıcı botunun sesi kapatıldı.**\n\n• **Userbot'un sesini açmak için şunu kullanın:**\n» /unmute komut."
            )
        except Exception as e:
            await m.reply(f"🚫 **ʜᴀᴛᴀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ʜɪᴄ ʙɪʀsᴇʏ ᴄᴀʟᴍɪʏᴏʀ**")


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
                "🔊 **Kullanıcı botunun sesi açıldı.**\n\n• **Userbot'un sesini kapatmak için**\n» /mute."
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("❌ **ʜɪᴄ ʙɪʀsᴇʏ ᴄᴀʟᴍɪʏᴏʀ**")


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Yalnızca bu düğmeye dokunabilen görüntülü sohbet yönetme iznine sahip yönetici !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.answer("streaming paused")
            await query.edit_message_text(
                "⏸ ᴀᴋɪs ᴅᴜʀᴅᴜʀᴜʟᴅᴜ", reply_markup=back_mark
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀᴏʀ:**\n\n`{e}`", reply_markup=close_mark)
    else:
        await query.answer("❌ sᴜ ᴀɴᴅᴀ ʜɪᴄʙɪʀ sᴇʏ ʏᴀʏɪɴʟᴀɴᴍɪʏᴏʀ", show_alert=True)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Yalnızca bu düğmeye dokunabilen görüntülü sohbet yönetme iznine sahip yönetici !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.answer("streaming resumed")
            await query.edit_message_text(
                "▶️ ᴀᴋɪs ʏᴇɴɪᴅᴇɴ ʙᴀsʟᴀᴛɪʟᴅɪ", reply_markup=back_mark
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀᴏʀ:**\n\n`{e}`", reply_markup=close_mark)
    else:
        await query.answer("❌ sᴜ ᴀɴᴅᴀ ʜɪᴄʙɪʀ sᴇʏ ʏᴀʏɪɴʟᴀɴᴍɪʏᴏʀ", show_alert=True)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Yalnızca bu düğmeye dokunabilen görüntülü sohbet yönetme iznine sahip yönetici !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text("✅ **ʙᴜ ᴀᴋɪs sᴏɴᴀ ᴇʀᴅɪ**", reply_markup=close_mark)
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀᴏʀ:**\n\n`{e}`", reply_markup=close_mark)
    else:
        await query.answer("❌ sᴜ ᴀɴᴅᴀ ʜɪᴄʙɪʀ sᴇʏ ʏᴀʏɪɴʟᴀɴᴍɪʏᴏʀ", show_alert=True)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Yalnızca bu düğmeye dokunabilen görüntülü sohbet yönetme iznine sahip yönetici !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.answer("streaming muted")
            await query.edit_message_text(
                "🔇 userbot başarıyla kapatıldı", reply_markup=back_mark
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ᴇʀᴏʀ:**\n\n`{e}`", reply_markup=close_mark)
    else:
        await query.answer("❌ sᴜ ᴀɴᴅᴀ ʜɪᴄʙɪʀ sᴇʏ ʏᴀʏɪɴʟᴀɴᴍɪʏᴏʀ", show_alert=True)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Yalnızca bu düğmeye dokunabilen görüntülü sohbet yönetme iznine sahip yönetici !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.answer("streaming unmuted")
            await query.edit_message_text(
                "🔊 userbot başarıyla açıldı", reply_markup=back_mark
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **ʜᴀᴛᴀ:**\n\n`{e}`", reply_markup=close_mark)
    else:
        await query.answer("❌ sᴜ ᴀɴᴅᴀ ʜɪᴄʙɪʀ sᴇʏ ʏᴀʏɪɴʟᴀɴᴍɪʏᴏʀ", show_alert=True)


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
                f"✅ **sᴇs sᴇᴠɪʏᴇsɪ** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"🚫 **ʜᴀᴛᴀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ᴀᴋɪsᴛᴀ ʜɪᴄʙɪʀ sᴇʏ ʏᴏᴋ**")
