from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

study_status = False
study_reason = ""
study_trigger_time = 0  # Timestamp of Study activation

@client.on(events.NewMessage(pattern=r"^\.help_study$", outgoing=True))
async def help_study(event):
    """Sends a help message explaining how to use the Study feature."""
    help_message = (
        "📚 **Study Help** 📚\n\n"
        "Welcome to the **Study Mode** guide! Here's how to use it:\n\n"
        "1. **Set yourself in Study Mode**: Use `.study` to set your status as Studying...\n"
        "2. **Set a custom Study message**: Use `.study <Subject>/What?` to specify a custom message when someone tries to message you while you're away Studying..\n"
        "3. **Remove Study status**: Use `.back_study` to remove the Study status and let others know you're back!\n\n"
        "🛑 **Important**: When you're Studying, anyone who messages you will see your Study message, so let them know you're studying!\n\n"
        "💡 **Pro Tip**: Use a friendly message to let people know you'll reply as soon as you're back! 😎"
    )
    await event.edit(help_message)
    
@client.on(events.NewMessage(pattern=r"^.study( .*)?", outgoing=True))
async def study(event):
    global study_status, study_reason, study_trigger_time
    
    # Prevent immediate disabling by tracking time
    study_trigger_time = time.time()
    
    study_status = True
    study_reason = event.pattern_match.group(1).strip() if event.pattern_match.group(1) else ""
    
    await event.edit(f"🚀 **Study Mode Enabled!**\n\n**I'll be back soon!** 🕒")

@client.on(events.NewMessage(incoming=True))
async def study_response(event):
    global study_status, study_reason
    if study_status and event.mentioned:
        await event.reply(f" **I'm Currently Studying..!**\n\nI'll respond when I'm back!**")

@client.on(events.NewMessage(outgoing=True))
async def disable_study(event):
    global study_status, study_trigger_time
    
    # Prevent Mode from disabling immediately after enabling
    if study_status and time.time() - study_trigger_time > 2:  # Wait at least 2 seconds
        # Send a new message when coming online and delete it in 2 seconds
        await event.respond("🚀 **Owner is now back online!** 🕒\nI'm ready to assist you! 😊")
        time.sleep(1)
        await event.delete()
        
        # Disable AFK mode
        study_status = False
