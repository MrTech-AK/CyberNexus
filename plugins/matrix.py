import time
from telethon import events
from cybernexus import client

@client.on(events.NewMessage(pattern=r"^\.matrix$", outgoing=True))
def matrix_animation(event):
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
        event.edit(frame)
        time.sleep(0.3)
