import os
import logging
import dotenv

from quart import Quart
import hypercorn.asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

dotenv.load_dotenv()

API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
SESSION = StringSession(os.environ.get('SESSION_STRING'))

client = TelegramClient(SESSION, API_ID, API_HASH)

app = Quart(__name__)
app.secret_key = 'CHANGE THIS TO SOMETHING SECRET'

logging.basicConfig(level=logging.INFO)
logging.getLogger('telethon').setLevel(level=logging.INFO)


@app.before_serving
async def startup():
    await client.connect()


@app.after_serving
async def cleanup():
    await client.disconnect()


async def main():
    await hypercorn.asyncio.serve(app, hypercorn.Config())


if __name__ == '__main__':
    client.loop.run_until_complete(main())
