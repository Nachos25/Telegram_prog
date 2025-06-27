import os
from datetime import datetime, timedelta
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('TG_API_ID')
API_HASH = os.getenv('TG_API_HASH')
SESSION = 'anon'

# Получить последние 10 чатов и сообщения за месяц

def fetch_recent_dialogs():
    print('Авторизация в Telegram...')
    client = TelegramClient(SESSION, API_ID, API_HASH)
    client.start()
    dialogs = []

    async def main():
        async for dialog in client.iter_dialogs(limit=10):
            if dialog.is_user or dialog.is_group or dialog.is_channel:
                messages = []
                month_ago = datetime.now() - timedelta(days=30)
                async for msg in client.iter_messages(
                    dialog.id, offset_date=None, reverse=True
                ):
                    if msg.date < month_ago:
                        break
                    messages.append(msg)
                dialogs.append({
                    'id': dialog.id,
                    'name': dialog.name,
                    'messages': messages,
                    'is_user': dialog.is_user
                })

    with client:
        client.loop.run_until_complete(main())
    return dialogs 