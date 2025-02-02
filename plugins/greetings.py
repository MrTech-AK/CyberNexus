from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

welcome_message = None
goodbye_message = None

# Help command for greetings
@client.on(events.NewMessage(pattern=r"^\.help_greetings$", outgoing=True))
async def help_greetings(event):
    """Displays a help message for the greetings feature."""
    help_message = (
        "📚 **Greetings Help** 📚\n\n"
        "Here are the commands you can use to manage welcome and goodbye messages:\n\n"
        "1. **Set welcome message**: `.setwelcome <your message>` to set a custom welcome message.\n"
        "2. **Clear welcome message**: `.clearwelcome` to clear the current welcome message.\n"
        "3. **Get welcome message**: `.getwelcome` to see the current welcome message.\n"
        "4. **Set goodbye message**: `.setgoodbye <your message>` to set a custom goodbye message.\n"
        "5. **Clear goodbye message**: `.cleargoodbye` to clear the current goodbye message.\n"
        "6. **Get goodbye message**: `.getgoodbye` to see the current goodbye message.\n"
        "7. **Enable/Disable thank you message**: `.thankmembers on` or `.thankmembers off` to toggle thank you messages for new members.\n\n"
        "🔄 **Note**: The **thank you** message is automatically sent when new members join the group, depending on your settings."
    )
    await event.edit(help_message)

# Set welcome message
@client.on(events.NewMessage(pattern=r"^\.setwelcome$", outgoing=True))
async def setwelcome(event):
    """Set the welcome message."""
    global welcome_message
    welcome_message = event.text.split(None, 1)[1] if len(event.text.split()) > 1 else "Welcome! 🎉"
    await event.edit(f"🎉 **Welcome message set to:** {welcome_message}")

# Clear welcome message
@client.on(events.NewMessage(pattern=r"^\.clearwelcome$", outgoing=True))
async def clearwelcome(event):
    """Clear the welcome message."""
    global welcome_message
    welcome_message = None
    await event.edit("❌ **Welcome message cleared.**")

# Get current welcome message
@client.on(events.NewMessage(pattern=r"^\.getwelcome$", outgoing=True))
async def getwelcome(event):
    """Get the current welcome message."""
    if welcome_message:
        await event.edit(f"🔍 **Current welcome message:** {welcome_message}")
    else:
        await event.edit("⚠️ **No welcome message set.**")

# Set goodbye message
@client.on(events.NewMessage(pattern=r"^\.setgoodbye$", outgoing=True))
async def setgoodbye(event):
    """Set the goodbye message."""
    global goodbye_message
    goodbye_message = event.text.split(None, 1)[1] if len(event.text.split()) > 1 else "Goodbye! 👋"
    await event.edit(f"👋 **Goodbye message set to:** {goodbye_message}")

# Clear goodbye message
@client.on(events.NewMessage(pattern=r"^\.cleargoodbye$", outgoing=True))
async def cleargoodbye(event):
    """Clear the goodbye message."""
    global goodbye_message
    goodbye_message = None
    await event.edit("❌ **Goodbye message cleared.**")

# Get current goodbye message
@client.on(events.NewMessage(pattern=r"^\.getgoodbye$", outgoing=True))
async def getgoodbye(event):
    """Get the current goodbye message."""
    if goodbye_message:
        await event.edit(f"🔍 **Current goodbye message:** {goodbye_message}")
    else:
        await event.edit("⚠️ **No goodbye message set.**")

# Enable or disable thank members message
@client.on(events.NewMessage(pattern=r"^\.thankmembers (on|off)$", outgoing=True))
async def thankmembers(event):
    """Enable or disable the thank you message when someone joins."""
    status = event.pattern_match.group(1)
    if status == "on":
        # Enable thank you message logic
        await event.edit("🎉 **Thank members message enabled.**")
    else:
        # Disable thank you message logic
        await event.edit("❌ **Thank members message disabled.**")
