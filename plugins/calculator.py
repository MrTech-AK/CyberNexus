from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

@client.on(events.NewMessage(pattern=r"^\.calc$", outgoing=True))
async def calc(event):
    """Open a simple calculator."""
    await event.edit("**Welcome to the calculator!**\nYou can now use simple mathematical expressions like:\n`2 + 2`, `3 * 5`, etc.\n**Type your expression below and I'll calculate it for you.**")
