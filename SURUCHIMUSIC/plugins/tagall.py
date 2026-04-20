import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait

# Stop system (better use set)
TAG_STOP = set()

@Client.on_message(filters.command(["tagall", "utag"]) & filters.group)
async def tag_all_members(client: Client, message: Message):
    chat_id = message.chat.id

    # Admin check
    user = await client.get_chat_member(chat_id, message.from_user.id)
    if user.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return await message.reply("❌ Only admins can use this!")

    # Tag text
    if len(message.command) < 2:
        tag_text = "Hey, wake up!"
    else:
        tag_text = message.text.split(None, 1)[1]

    # Remove stop flag if exists
    TAG_STOP.discard(chat_id)

    await message.reply("✨ Tagging started...\nUse /cancel to stop.")

    members = []

    # Fetch members safely
    async for member in client.get_chat_members(chat_id):
        if member.user and not member.user.is_bot:
            name = member.user.first_name
            user_id = member.user.id
            members.append(f"[{name}](tg://user?id={user_id})")

    count = 0

    # Send in batches of 5
    for i in range(0, len(members), 5):
        if chat_id in TAG_STOP:
            break

        batch = members[i:i+5]
        text = f"📢 **{tag_text}**\n\n" + " ".join(batch)

        try:
            await client.send_message(
                chat_id,
                text,
                parse_mode="markdown"
            )
            count += len(batch)
            await asyncio.sleep(3)

        except FloodWait as e:
            await asyncio.sleep(e.value)

        except Exception as e:
            print(e)

    # Final message
    if chat_id in TAG_STOP:
        TAG_STOP.discard(chat_id)
        await message.reply(f"🚫 Tagging stopped!\nTotal tagged: {count}")
    else:
        await message.reply(f"✅ Done!\nTotal tagged: {count}")


@Client.on_message(filters.command(["cancel", "stopall"]) & filters.group)
async def stop_tagging(client: Client, message: Message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)

    if user.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return

    TAG_STOP.add(message.chat.id)
    await message.reply("⏳ Stopping tagall...")