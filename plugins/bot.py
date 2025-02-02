import os
import sys
import time
import platform
import telethon
from telethon import TelegramClient, events, Button
import config

# Initialize the bot
bot = TelegramClient("CyberNexus", config.API_ID, config.API_HASH).start(bot_token=config.BOT_TOKEN)

# Get environment details
DEPLOYER_NAME = config.DEPLOYER_NAME if hasattr(config, "DEPLOYER_NAME") else "Unknown User"
PYTHON_VERSION = platform.python_version()
TELETHON_VERSION = telethon.__version__

# ─────────── 🌐 HELP MENU ─────────── #
HELP_TEXT = {
    "alive": "🔹 **.alive** → Check bot status & details.",
    "ping": "🔹 **.ping** → Check bot latency.",
    "restart": "🔹 **.restart** → Restart the bot.",
}

# ─────────── 🔴 ALIVE COMMAND ─────────── #
@bot.on(events.NewMessage(pattern="^.alive$"))
async def alive(event):
    alive_msg = f"""
🌐 **ᴄʏʙᴇʀɴᴇxᴜs | ᴏɴʟɪɴᴇ** 🌐

✵ **Owner:** {DEPLOYER_NAME} 👑  
✵ **Nexus:** v1.0  
✵ **Py-Nexus:** 2025  
✵ **Uptime:** Aʟɪᴠᴇ & ᴡᴇʟʟ ⏳  
✵ **Python:** v{PYTHON_VERSION} 🐍  
✵ **Telethon:** v{TELETHON_VERSION} 📡  
✵ **Branch:** main ⚙️
"""
    await event.reply(alive_msg, buttons=[Button.inline("🆘 Help", data="alive_help")])

# ─────────── 🟢 PING COMMAND ─────────── #
@bot.on(events.NewMessage(pattern="^.ping$"))
async def ping(event):
    start = time.time()
    msg = await event.reply("🏓 **Pong!**")
    end = time.time()
    latency = round((end - start) * 1000, 2)
    await msg.edit(f"🏓 **Pong!** `{latency}ms`")

# ─────────── 🆘 HELP COMMANDS (INLINE) ─────────── #
@bot.on(events.NewMessage(pattern="^.alivehelp$"))
async def alive_help(event):
    await event.reply("🆘 **Alive Help Menu**", buttons=[Button.inline("ℹ View Details", data="alive_help")])

@bot.on(events.NewMessage(pattern="^.pinghelp$"))
async def ping_help(event):
    await event.reply("🆘 **Ping Help Menu**", buttons=[Button.inline("ℹ View Details", data="ping_help")])


# ─────────── 📜 INLINE HELP MENU ─────────── #
@bot.on(events.CallbackQuery(data=b"alive_help"))
async def alive_help_cb(event):
    await event.edit(HELP_TEXT["alive"], buttons=[Button.inline("🔙 Back", data="back")])

@bot.on(events.CallbackQuery(data=b"ping_help"))
async def ping_help_cb(event):
    await event.edit(HELP_TEXT["ping"], buttons=[Button.inline("🔙 Back", data="back")])


@bot.on(events.CallbackQuery(data=b"back"))
async def back_cb(event):
    await event.edit("🆘 **Choose a help menu:**", buttons=[
        [Button.inline("📡 Alive Help", data="alive_help")],
        [Button.inline("🏓 Ping Help", data="ping_help")],
     ])

# Start the bot
print("✅ CyberNexus Bot is running...")
bot.run_until_disconnected()
