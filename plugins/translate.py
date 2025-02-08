from googletrans import Translator
from telethon import events
from cybernexus import client
import platform 

@client.on(events.NewMessage(pattern=r"^\.tr (\w+) (.+)", outgoing=True))
async def translate(event):
    """Translate text to another language."""
    args = event.pattern_match.group(1).lower()
    text = event.pattern_match.group(2)
    
    await event.edit("🌍 **Translating... Please wait...**")
    
    translator = Translator()
    try:
        translated_text = translator.translate(text, dest=args)
        lang = translated_text.src.upper()
        target_lang = translated_text.dest.upper()
        
        message = (
            "📝 **Translation Completed!**\n\n"
            f"🔹 **Original ({lang}):** `{text}`\n"
            f"🔸 **Translated ({target_lang}):** `{translated_text.text}`\n\n"
            "⚡ Powered by CyberNexus"
        )
        await event.edit(message)
    
    except Exception as e:
        await event.edit(f"❌ **Translation failed:** `{str(e)}`")
