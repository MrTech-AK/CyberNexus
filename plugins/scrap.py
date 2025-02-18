from telethon import events
from cybernexus import client
import config
import time
import sys
import telethon
from telethon import events
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors import UserPrivacyRestrictedError, FloodWaitError, ChatAdminRequiredError, ChatWriteForbiddenError
import asyncio
import platform 

@client.on(events.NewMessage(pattern=r"^.scrap @(\S+) @(\S+)", outgoing=True))
async def scrape_and_add(event):
    args = event.pattern_match.groups()
    from_group = args[0]
    to_group = args[1]

    msg = await event.reply(f"🔍 **Scraping members from** `{from_group}`...")

    try:
        from_entity = await client.get_entity(from_group)
        to_entity = await client.get_entity(to_group)

        members = await client.get_participants(from_entity)
        total_members = len(members)

        if total_members == 0:
            return await msg.edit("🚫 **No members found in the source group.**")

        await msg.edit(f"📦 **Found {total_members} members. Adding to {to_group}...**")

        added_count, failed_count = 0, 0

        for user in members:
            if user.bot or user.deleted:
                continue  # Skip bots & deleted accounts

            try:
                await client(InviteToChannelRequest(to_entity, [user.id]))
                added_count += 1
                await asyncio.sleep(5)  # Prevent rate limits
            except UserPrivacyRestrictedError:
                failed_count += 1  # Skipping users with private settings
            except ChatAdminRequiredError:
                return await msg.edit("⚠️ **I need admin rights to add members to this group!**")
            except ChatWriteForbiddenError:
                return await msg.edit("⚠️ **I don't have permission to add members!**")
            except FloodWaitError as e:
                await msg.edit(f"🚨 **Rate limit hit! Waiting {e.seconds} seconds...**")
                await asyncio.sleep(e.seconds)
            except:
                failed_count += 1
                continue

            if added_count % 10 == 0:
                await msg.edit(f"✅ **Added:** `{added_count}/{total_members}` | ❌ **Failed:** `{failed_count}`")

        await msg.edit(f"🎯 **Scraping Complete!** ✅ **Added:** `{added_count}` | ❌ **Failed:** `{failed_count}`")

    except ValueError:
        await msg.edit("❌ **Invalid group or channel username!** Check the usernames and try again.")
    except Exception as e:
        await msg.edit(f"❌ **Error:** `{str(e)}`\n_Ensure both groups exist & I have admin rights._")
