from telethon import events
from cybernexus import client
import aiohttp
import platform 

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

@client.on(events.NewMessage(pattern=r"^\.define\s+(.+)", outgoing=True))
async def define_word(event):
    """Fetches the meaning of a word."""
    word = event.pattern_match.group(1).strip()

    await event.edit(f"📖 **Searching for:** `{word}`...")

    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL + word) as response:
            if response.status != 200:
                return await event.edit(f"❌ **No definition found for:** `{word}`!")

            data = await response.json()
            meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
            example = data[0]["meanings"][0]["definitions"][0].get("example", "No example available.")
            phonetic = data[0].get("phonetic", "N/A")

            reply = (
                f"📖 **Word:** `{word}`\n"
                f"🔊 **Phonetic:** `{phonetic}`\n"
                f"📚 **Definition:** {meaning}\n"
                f"💬 **Example:** {example}\n\n"
                f"⚡ **Powered by CyberNexus**"
            )

    await event.edit(reply)


@client.on(events.NewMessage(pattern=r"^\.syn\s+(.+)", outgoing=True))
async def synonyms(event):
    """Fetches synonyms of a word."""
    word = event.pattern_match.group(1).strip()

    await event.edit(f"🔵 **Fetching synonyms for:** `{word}`...")

    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL + word) as response:
            if response.status != 200:
                return await event.edit(f"❌ **No synonyms found for:** `{word}`!")

            data = await response.json()
            syns = data[0]["meanings"][0].get("synonyms", [])

            if not syns:
                return await event.edit(f"❌ **No synonyms available for:** `{word}`!")

            await event.edit(f"🔵 **Synonyms of `{word}`:**\n`{', '.join(syns[:10])}`\n\n⚡ **Powered by CyberNexus**")


@client.on(events.NewMessage(pattern=r"^\.ant\s+(.+)", outgoing=True))
async def antonyms(event):
    """Fetches antonyms of a word."""
    word = event.pattern_match.group(1).strip()

    await event.edit(f"🔴 **Fetching antonyms for:** `{word}`...")

    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL + word) as response:
            if response.status != 200:
                return await event.edit(f"❌ **No antonyms found for:** `{word}`!")

            data = await response.json()
            ants = data[0]["meanings"][0].get("antonyms", [])

            if not ants:
                return await event.edit(f"❌ **No antonyms available for:** `{word}`!")

            await event.edit(f"🔴 **Antonyms of `{word}`:**\n`{', '.join(ants[:10])}`\n\n⚡ **Powered by CyberNexus**")
