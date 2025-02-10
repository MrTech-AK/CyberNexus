from telethon import events
from bot import bot

@bot.on(events.NewMessage(incoming=True, chats="CONTACT_BOT_GROUPS", reply_to=True))
async def admin_reply(event):
    replied_msg = await event.get_reply_message()
    
    if replied_msg and replied_msg.forward and replied_msg.forward.original_fwd:
        user_id = replied_msg.forward.original_fwd.from_id.user_id

        if user_id:
            reply_text = f"📩 **Admin Reply:**\n\n{event.text}"
            await bot.send_message(user_id, reply_text)
            await event.reply("✅ **Reply sent successfully!**")
        else:
            await event.reply("❌ **Error: Unable to find user ID.**")
