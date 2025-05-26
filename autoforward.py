import os
import asyncio
from telethon import TelegramClient

# Use the same session name you used earlier
client = TelegramClient('forward_by_link_session', api_id=int(os.getenv('API_ID')), api_hash=os.getenv('API_HASH'))

# Set these values
source_channel = 'dauntlessly'  # Username or ID of source channel
message_id = 535             # ID of the message to forward

# List of target chats and topic IDs (for threaded groups)
target_chats = [
    ('@janehcbe', 6),
    ('@skidtxt', 4)
]

async def forward_post():
    msg = await client.get_messages(source_channel, ids=message_id)
    for chat, topic_id in target_chats:
        try:
            await client.forward_messages(
                entity=chat,
                messages=msg,
                thread=topic_id  # topic/thread ID (only for groups with topics enabled)
            )
            print(f"Forwarded to topic {topic_id} in {chat}")
        except Exception as e:
            print(f"Failed to forward to {chat}: {e}")

async def main():
    await client.start()
    await forward_post()

if __name__ == '__main__':
    asyncio.run(main())
