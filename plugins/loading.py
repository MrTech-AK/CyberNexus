import time
from telethon import events
from cybernexus import client

@client.on(events.NewMessage(pattern=r"^\.loading$", outgoing=True))
def loading_animation(event):
    """CyberNexus Super Extended Loading Effect"""
    
    animation = [
        "`Loading [░░░░░░░░░░] 0%`",
        "`Loading [▓░░░░░░░░░] 5%`",
        "`Loading [▓▓░░░░░░░░] 10%`",
        "`Loading [▓▓▓░░░░░░░] 15%`",
        "`Loading [▓▓▓▓░░░░░░] 20%`",
        "`Loading [▓▓▓▓▓░░░░░] 30%`",
        "`Loading [▓▓▓▓▓▓░░░░] 40%`",
        "`Loading [▓▓▓▓▓▓▓░░░] 50%`",
        "`Loading [▓▓▓▓▓▓▓▓░░] 60%`",
        "`Loading [▓▓▓▓▓▓▓▓▓░] 70%`",
        "`Loading [▓▓▓▓▓▓▓▓▓▓] 80%`",
        "`Loading [█████████░] 90%`",
        "`Loading [██████████] 95%`",
        "`Loading Complete... Finalizing`",
        "`✅ Loading Complete!`"
    ]

    for frame in animation:
        event.edit(frame)
        time.sleep(0.4)
