from telethon import TelegramClient, events, Button
import config  # Import API credentials

# Initialize the bot client
bot = TelegramClient("contact_bot", config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN)

# Your Telegram User ID (To receive forwarded messages)
OWNER_ID = config.OWNER_ID  # Replace with your Telegram ID

# Start command with cool UI
@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    buttons = [
        [Button.url("📞 Contact Admin", f"tg://user?id={OWNER_ID}")],
        [Button.url("🌐 Visit Website", "https://github.com/MrTech-AK")],
    ]
    await event.respond(
        "👋 **Welcome to CyberNexus Contact Bot!**\n\n📩 Send your message, and I will forward it to my Owner!",
        buttons=buttons
    )

# Forward user messages to Admin
@bot.on(events.NewMessage)
async def forward_to_admin(event):
    if event.is_private and event.sender_id != OWNER_ID:
        msg = f"📩 **New Message from:** [{event.sender.first_name}](tg://user?id={event.sender_id})\n\n{event.message.text}"
        await bot.send_message(OWNER_ID, msg)
        await event.respond("✅ **Your message has been sent to the admin!**")

# Admin replies to users
@bot.on(events.NewMessage(from_users=OWNER_ID, pattern="^/reply (\\d+) (.+)"))
async def reply_to_user(event):
    args = event.pattern_match.groups()
    user_id = int(args[0])
    reply_text = args[1]

    await bot.send_message(user_id, f"📩 **Admin's Reply:**\n{reply_text}")
    await event.respond("✅ **Reply sent successfully!**")

# Run the bot
print("🤖 CyberNexus Contact Bot is Online!")
bot.run_until_disconnected()
