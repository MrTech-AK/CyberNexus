from telethon import events
from cybernexus import client
import platform 

@client.on(events.NewMessage(pattern=r"^\.calc (.+)$", outgoing=True))
async def calculator(event):
    """Evaluates a math expression."""
    expression = event.pattern_match.group(1)

    try:
        result = eval(expression)
        await event.edit(f"🧮 **Calculation:** `{expression}`\n📊 **Result:** `{result}`\n\n⚡ Powered By CyberNexus")
    except Exception as e:
        await event.edit(f"❌ **Error:** `{str(e)}`")
