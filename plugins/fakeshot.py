from telethon import events
from cybernexus import client
import time
import platform 

@client.on(events.NewMessage(pattern=r"^\.fakeshot (.+)$", outgoing=True))
def fake_screenshot(event):
    """CyberNexus Fake Telegram Screenshot Generator"""
    
    try:
        args = event.pattern_match.group(1).split("|")
        chat_name = args[0].strip()
        messages = [msg.strip() for msg in args[1:]]

        fake_screenshot = f"📸 **Fake Screenshot**\n👤 {chat_name}\n"
        for msg in messages:
            fake_screenshot += f"💬 {msg}\n"

        event.edit(fake_screenshot)

    except Exception as e:
        event.edit("❌ **Usage:** `.fakeshot <name> | <msg1> | <msg2>`")
