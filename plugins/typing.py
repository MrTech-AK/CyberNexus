import time
from telethon import events
from cybernexus import client

@client.on(events.NewMessage(pattern=r"^\.typing (.+)$", outgoing=True))
def typing_effect(event):
    """CyberNexus Typing Effect Animation"""

    text = event.pattern_match.group(1)  # Get the text after .typing
    typing_message = ""

    for char in text:
        typing_message += char
        event.edit(typing_message + "▌")  # Simulate typing cursor
        time.sleep(0.1)  # Adjust speed for realism

    event.edit(typing_message)  # Remove cursor at the end
