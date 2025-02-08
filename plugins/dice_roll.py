from telethon import events
from cybernexus import client
import random
import platform 

@client.on(events.NewMessage(pattern=r"^\.dice$", outgoing=True))
async def roll_dice(event):
    """CyberNexus Dice Roller"""
    
    dice_face = random.randint(1, 6)
    dice_art = {
        1: "⚀", 2: "⚁", 3: "⚂",
        4: "⚃", 5: "⚄", 6: "⚅"
    }
    
    await event.edit(f"🎲 **You rolled:** {dice_face} {dice_art[dice_face]}")
