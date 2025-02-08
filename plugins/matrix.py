from telethon import events
from cybernexus import client
import asyncio  # ✅ Use asyncio instead of time.sleep()
import platform 

@client.on(events.NewMessage(pattern=r"^\.matrix$", outgoing=True))
async def matrix_animation(event):
    """CyberNexus Extended Matrix Effect"""
    
    animation = [
        "`⡿⠋⣀⠀⢀⣀⣀⡀⠀⠈⠙⢿`",
        "`⡇⢠⠇⢀⣾⡿⠿⢿⣦⠀⢹`",
        "`⣷⢳⠀⠈⠉⠀⠀⠀⠉⠀⡾`",
        "`⠹⣄⡀⠀⠀⠀⢀⣠⡞`",
        "`⠀⠙⠻⠶⠶⠿⠟⠁`",
        "`Wake up, CyberNexus...`",
        "`The Matrix has you...`",
        "`Follow the White Rabbit...`",
        "`Knock, knock...`",
        "`Connecting to the Grid...`",
        "`Decrypting System Files...`",
        "`Accessing Hidden Nodes...`",
        "`⡿⠋⣀⠀⢀⣀⣀⡀⠀⠈⠙⢿`",
        "`Entering the Mainframe...`",
        "`Hacking into the core system...`",
        "`Upload complete!`"
    ]

    for frame in animation:
        await event.edit(frame)  # ✅ Corrected `await`
        await asyncio.sleep(0.3)  # ✅ Replaced `time.sleep()` with `asyncio.sleep()`
