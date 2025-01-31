from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
import platform

notes = {}

@client.on(events.NewMessage(pattern=r"^\.addnote( (.*)|$)", outgoing=True))
async def addnote(event):
    """Add a note."""
    note = event.pattern_match.group(1) if event.pattern_match.group(1) else "No content provided."
    note_id = len(notes) + 1
    notes[note_id] = note
    await event.edit(f"**Note added with ID {note_id}:**\n{note}")

@client.on(events.NewMessage(pattern=r"^\.remnote( (.*)|$)", outgoing=True))
async def remnote(event):
    """Remove a note by ID."""
    note_id = int(event.pattern_match.group(1) if event.pattern_match.group(1) else -1)
    if note_id in notes:
        removed_note = notes.pop(note_id)
        await event.edit(f"**Note with ID {note_id} removed.**\n{removed_note}")
    else:
        await event.edit("**Note ID not found.**")

@client.on(events.NewMessage(pattern=r"^\.listnote$", outgoing=True))
async def listnote(event):
    """List all notes."""
    if notes:
        note_list = "\n".join([f"{id}: {note}" for id, note in notes.items()])
        await event.edit(f"**Current notes:**\n{note_list}")
    else:
        await event.edit("**No notes available.**")
