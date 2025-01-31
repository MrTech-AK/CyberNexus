from telethon import TelegramClient, events
from telethon.sessions import StringSession  # Import StringSession
import config  # Import config.py

# Initialize Telegram Client using StringSession
client = TelegramClient(
    session=StringSession(config.STRING_SESSION),  # Ensure StringSession is used
    api_id=config.API_ID,
    api_hash=config.API_HASH
)

# Start the client
async def start_bot():
    await client.start()
    print("✅ CyberNexus Userbot is Online!")
    
    # Set custom bio/status message (optional)
    await client(UpdateProfileRequest(about="ᴄʏʙᴇʀɴᴇxᴜs | ᴏɴʟɪɴᴇ 🌐"))

# Event handler for `.alive` command
@client.on(events.NewMessage(pattern=r"^.alive$", outgoing=True))
async def alive(event):
    cyber_alive_text = (
        "🌐 **ᴄʏʙᴇʀɴᴇxᴜs | ᴏɴʟɪɴᴇ** 🌐\n\n"
        f"✵ **Owner:** {config.DEPLOYER_NAME} 👑\n"
        "✵ **Nexus:** v1.0\n"
        "✵ **Py-Nexus:** 2025\n"
        "✵ **Uptime:** Aʟɪᴠᴇ & ᴡᴇʟʟ ⏳\n"
        f"✵ **Python:** v{platform.python_version()} 🐍\n"
        f"✵ **Telethon:** v{TelegramClient.__version__} 📡\n"
        "✵ **Branch:** master ⚙️"
    )

    await event.edit(cyber_alive_text)  # Edit the command message instead of sending a new one

# Run the bot
with client:
    client.loop.run_until_complete(start_bot())
    client.run_until_disconnected()
