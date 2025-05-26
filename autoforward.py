import os
import asyncio
from telethon import TelegramClient

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
source_channel = 'dauntlessly'
message_id = 535
target_chats = [
    ('@sectormarket', 18),  # example topic IDs
    ('@social', 13),
    ('@marketogs', 127884),
    ('@oguflip', 11196),
    ('@blackmarket', 16),
    ('@LuxurMarket', 21),
    ('@texted', 7)
]

client = TelegramClient('forward_by_link_session', api_id, api_hash)

async def forward_post():
    try:
        msg = await client.get_messages(source_channel, ids=message_id)

        for chat, topic_id in target_chats:
            try:
                await client.send_message(chat, msg, reply_to=topic_id)
                print(f"Forwarded to topic {topic_id} in {chat}")
            except Exception as e:
                print(f"Failed to forward to {chat}: {e}")
    except Exception as e:
        print(f"Failed to get message: {e}")

async def periodic_forward():
    await client.start()
    print("Bot started. Beginning periodic forwarding...")

    while True:
        await forward_post()
        print("Waiting 1 hour before next forwarding...")
        await asyncio.sleep(3600)  # Sleep for 1 hour (3600 seconds)

async def main():
    await periodic_forward()

if __name__ == '__main__':
    client.loop.run_until_complete(main())
