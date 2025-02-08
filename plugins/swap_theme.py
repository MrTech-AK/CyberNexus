from telethon import events
from cybernexus import client

@client.on(events.NewMessage(pattern=r"^\.swaptheme$", outgoing=True))
async def swap_theme(event):
    """CyberNexus Dark x Light Mode Swapper"""
    await event.edit("🔄 **Swapping Telegram Theme...**")
    await client.send_message("Telegram", "/settheme Night" if "Day" in event.text else "/settheme Day")
    await event.edit("✅ **Theme Switched!**")
