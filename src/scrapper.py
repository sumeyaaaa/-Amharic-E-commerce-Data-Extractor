# scraper.py

import os
import pandas as pd
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from config import api_id, api_hash, phone

# Initialize the Telegram client
client = TelegramClient('scraper_session', api_id, api_hash)

async def scrape_channel(channel_username, limit=100):
    await client.start(phone=phone)
    entity = await client.get_entity(channel_username)

    # Create folder for this channel's images
    image_folder = f"images/{channel_username.strip('@')}"
    os.makedirs(image_folder, exist_ok=True)

    # Get message history
    history = await client(GetHistoryRequest(
        peer=entity,
        limit=limit,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))

    messages = []
    for message in history.messages:
        if not message.message and not message.media:
            continue  # Skip messages with no text or image

        image_path = None
        if message.media and hasattr(message.media, 'photo'):
            filename = f"{channel_username}_{message.id}.jpg"
            image_path = os.path.join(image_folder, filename)
            await client.download_media(message.media, image_path)

        messages.append({
            'channel_title': entity.title,
            'channel_username': channel_username,
            'id': message.id,
            'text': message.message or "",
            'date': message.date,
            'sender_id': message.from_id.user_id if message.from_id else None,
            'views': message.views,
            'image_path': image_path
        })

    return messages


async def scrape_multiple(channels, output_path, limit=100):
    all_data = []
    for channel in channels:
        print(f"Scraping: {channel}")
        try:
            data = await scrape_channel(channel, limit=limit)
            all_data.extend(data)
        except Exception as e:
            print(f"❌ Failed to scrape {channel}: {e}")

    df = pd.DataFrame(all_data)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"✅ Saved all scraped data to: {output_path}")
