from telethon import events
from config import CONTACT_BOT_GROUPS, BLOCKED_KEYWORDS, BLOCKED_TYPES
from bot import bot

@bot.on(events.NewMessage(incoming=True))
async def forward_to_admins(event):
    if event.is_private:
        sender = await event.get_sender()
        user_info = f"📩 **New Message**\n👤 **From:** [{sender.first_name}](tg://user?id={sender.id})\n🆔 **User ID:** `{sender.id}`"

        if event.text and any(keyword in event.text.lower() for keyword in BLOCKED_KEYWORDS):
            await event.respond("❌ **Your message was blocked due to restricted content.**")
            return

        if event.file and event.file.ext in BLOCKED_TYPES:
            await event.respond("❌ **This type of media is not allowed.**")
            return

        for group in CONTACT_BOT_GROUPS:
            await bot.send_message(group, user_info)
            await bot.forward_messages(group, event.message)

        await event.respond("✅ **Your message has been sent to the admins!**")
