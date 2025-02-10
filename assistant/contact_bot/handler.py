from telethon import events
from config import CONTACT_BOT_GROUPS
from bot import bot

@bot.on(events.NewMessage(incoming=True))
async def forward_to_admin(event):
    if event.is_private:
        sender = await event.get_sender()
        msg = f"📩 **New Message Received**\n👤 **From:** [{sender.first_name}](tg://user?id={sender.id})\n🆔 **User ID:** `{sender.id}`"

        for group in CONTACT_BOT_GROUPS:
            await bot.send_message(group, msg)
            await bot.forward_messages(group, event.message)

        await event.respond("✅ **Your message has been sent to the admins! They will reply soon.**")
