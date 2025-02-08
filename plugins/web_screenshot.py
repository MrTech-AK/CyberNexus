from telethon import events
from cybernexus import client
import os

@client.on(events.NewMessage(pattern=r"^\.ss (.+)$", outgoing=True))
async def screenshot(event):
    """CyberNexus Web Screenshot Plugin"""
    
    url = event.pattern_match.group(1)
    file_path = "screenshot.png"
    
    await event.edit("📸 **Capturing Screenshot...**")
    
    os.system(f"webkit2png -o {file_path} {url}")  # Requires webkit2png installed
    
    if os.path.exists(file_path):
        await client.send_file(event.chat_id, file_path, caption=f"🌐 **Screenshot of {url}**")
        os.remove(file_path)
    else:
        await event.edit("❌ **Error capturing screenshot!**")
