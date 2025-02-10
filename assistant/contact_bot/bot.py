from telethon import TelegramClient, events, Button
from config import API_ID, API_HASH, BOT_TOKEN

# Initialize the bot
bot = TelegramClient("CyberNexus_ContactBot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Start Command with Inline Buttons
@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    buttons = [
        [Button.inline("📩 Contact Admin", data="contact_admin")],
        [Button.url("🌐 Visit Website", "https://yourwebsite.com")],
    ]
    start_text = (
        "🤖 **Cyber Nexus Contact Bot** 🤖\n\n"
        "🔹 **How It Works?**\n"
        "📩 Send me a message, and I'll forward it to the admins.\n"
        "💬 They will reply to you as soon as possible.\n\n"
        "🚀 **Powering Secure & Smart Communications!**\n\n"
        "⚡ **Powered by CyberNexus**"
    )
    await event.respond(start_text, buttons=buttons)

@bot.on(events.CallbackQuery(data="contact_admin"))
async def contact_admin(event):
    await event.edit("📩 **Send your message here, and I'll forward it to the admins!**")

# Run the bot
bot.run_until_disconnected()
