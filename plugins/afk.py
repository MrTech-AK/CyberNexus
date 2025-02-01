from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

afk_status = False
afk_reason = ""
afk_trigger_time = 0  # Timestamp of AFK activation

@client.on(events.NewMessage(pattern=r"^.afk( .*)?", outgoing=True))
async def afk(event):
    global afk_status, afk_reason, afk_trigger_time
    
    # Prevent immediate disabling by tracking time
    afk_trigger_time = time.time()
    
    afk_status = True
    afk_reason = event.pattern_match.group(1).strip() if event.pattern_match.group(1) else "No reason given."
    
    await event.edit(f"🚀 **AFK Mode Enabled!**\n📝 Reason: {afk_reason}")

@client.on(events.NewMessage(incoming=True))
async def afk_response(event):
    global afk_status, afk_reason
    if afk_status and event.mentioned:
        await event.reply(f"🤖 I'm currently AFK!\n📝 Reason: {afk_reason}")

@client.on(events.NewMessage(outgoing=True))
async def disable_afk(event):
    global afk_status, afk_trigger_time
    
    # Prevent AFK from disabling immediately after enabling
    if afk_status and time.time() - afk_trigger_time > 2:  # Wait at least 2 seconds
        afk_status = False
        await event.edit("✅ **AFK Mode Disabled!**")
