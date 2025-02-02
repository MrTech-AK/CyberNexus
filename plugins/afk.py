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

@client.on(events.NewMessage(pattern=r"^\.help_afk$", outgoing=True))
async def help_afk(event):
    """Sends a help message explaining how to use the AFK feature."""
    help_message = (
        "📚 **Owner AFK Help** 📚\n\n"
        "Welcome to the **AFK Mode** guide! Here's how to use it:\n\n"
        "1. **Set yourself as AFK**: Use `.afk` to set your status as away from keyboard.\n"
        "2. **Set a custom AFK message**: Use `.afk <your message>` to specify a custom message when someone tries to message you while you're away.\n"
        "3. **Remove AFK status**: Use `.back` to remove the AFK status and let others know you're back!\n\n"
        "🛑 **Important**: When you're AFK, anyone who messages you will see your AFK message, so let them know you're away!\n\n"
        "💡 **Pro Tip**: Use a friendly message to let people know you'll reply as soon as you're back! 😎"
    )
    await event.edit(help_message)
    
@client.on(events.NewMessage(pattern=r"^.afk( .*)?", outgoing=True))
async def afk(event):
    global afk_status, afk_reason, afk_trigger_time
    
    # Prevent immediate disabling by tracking time
    afk_trigger_time = time.time()
    
    afk_status = True
    afk_reason = event.pattern_match.group(1).strip() if event.pattern_match.group(1) else "No reason given."
    
    await event.edit(f"🚀 **Owner AFK Mode Enabled!**\n📝 **Reason**: {afk_reason}\n\n**I'll be back soon!** 🕒")

@client.on(events.NewMessage(incoming=True))
async def afk_response(event):
    global afk_status, afk_reason
    if afk_status and event.mentioned:
        await event.reply(f"🤖 **Owner is currently AFK!**\n📝 **Reason**: {afk_reason}\n**I'll respond when I'm back!** 😴")

@client.on(events.NewMessage(outgoing=True))
async def disable_afk(event):
    global afk_status, afk_trigger_time
    
    # Prevent AFK from disabling immediately after enabling
    if afk_status and time.time() - afk_trigger_time > 2:  # Wait at least 2 seconds
        # Send a new message when coming online and delete it in 2 seconds
        await event.respond("🚀 **Owner is now back online!** 🕒\nI'm ready to assist you! 😊")
        time.sleep(2)
        await event.delete()
        
        # Disable AFK mode
        afk_status = False
