from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform  # ✅ Fixed import

@client.on(events.NewMessage(pattern=r"^\.hack(?: |$)(.*)", outgoing=True))
def hack(event):
    """Ultimate Fake Hacking Animation (No Async)"""
    target = event.pattern_match.group(1) or "Target"

    animation = [
        f"🔍 Searching for {target}'s credentials...",
        "🔗 Establishing a secure connection to Dark Web...",
        "🟢 Connection established!",
        "📡 Connecting to Telegram servers...",
        "🔑 Bypassing login security...",
        "🔓 Password cracked: `********`",
        "🛠 Extracting saved passwords...",
        "🔍 Finding linked social media accounts...",
        "🔗 Facebook found! Hacking in progress...",
        "🔗 Instagram found! Downloading DMs...",
        "🔗 Twitter found! Fetching tweets...",
        "📂 Extracting private messages...",
        "📀 Downloading contact list...",
        "💳 Fetching credit card details...",
        "🧠 Running AI to analyze data...",
        "⚠ Detecting encrypted files... Attempting decryption...",
        "🔓 Decryption successful! Accessing hidden files...",
        "📡 GPS location detected! Tracking device...",
        "🖥 Activating front camera...",
        "📸 Capturing a live photo...",
        "📤 Uploading data to Dark Web...",
        "🛑 Oops! Telegram Security detected the breach! Retrying...",
        "🔄 Changing IP Address...",
        "🌍 Spoofing location...",
        "🗂 Cloning SIM card...",
        "📀 Extracting call logs...",
        "💰 Checking UPI transactions...",
        "🚀 Speeding up process...",
        "🛑 Admin detected the intrusion! Hiding tracks...",
        "✅ Hack successful! All data uploaded to Dark Web. ☠",
        f"⚠ **{target} has been hacked successfully!**\n💀 _All data is now public!_"
    ]

    for msg in animation:
        event.edit(msg)
        time.sleep(2)  # Normal sleep instead of asyncio
