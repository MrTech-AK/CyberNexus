from PyDictionary import PyDictionary
from telethon import events
from cybernexus import client
import platform 

dictionary = PyDictionary()

@client.on(events.NewMessage(pattern=r"^\.define (.+)", outgoing=True))
async def define_word(event):
    """Fetches the meaning of a word."""
    word = event.pattern_match.group(1)
    await event.edit(f"📖 **Searching for:** `{word}`...")

    try:
        meaning = dictionary.meaning(word)
        if not meaning:
            return await event.edit("❌ **No definition found!**")
        
        definition = "\n".join(f"• {key}: {', '.join(value)}" for key, value in meaning.items())
        await event.edit(f"📖 **Word:** `{word}`\n\n{definition}\n\n⚡ Powered by CyberNexus")
    except Exception as e:
        await event.edit(f"❌ **Error:** {str(e)}")


@client.on(events.NewMessage(pattern=r"^\.syn (.+)", outgoing=True))
async def synonyms(event):
    """Fetches synonyms of a word."""
    word = event.pattern_match.group(1)
    await event.edit(f"🔵 **Fetching synonyms for:** `{word}`...")

    try:
        syns = dictionary.synonym(word)
        if not syns:
            return await event.edit("❌ **No synonyms found!**")
        
        await event.edit(f"🔵 **Synonyms of `{word}`:**\n{', '.join(syns)}\n\n⚡ Powered by CyberNexus")
    except Exception as e:
        await event.edit(f"❌ **Error:** {str(e)}")


@client.on(events.NewMessage(pattern=r"^\.ant (.+)", outgoing=True))
async def antonyms(event):
    """Fetches antonyms of a word."""
    word = event.pattern_match.group(1)
    await event.edit(f"🔴 **Fetching antonyms for:** `{word}`...")

    try:
        ants = dictionary.antonym(word)
        if not ants:
            return await event.edit("❌ **No antonyms found!**")
        
        await event.edit(f"🔴 **Antonyms of `{word}`:**\n{', '.join(ants)}\n\n⚡ Powered by CyberNexus")
    except Exception as e:
        await event.edit(f"❌ **Error:** {str(e)}")
