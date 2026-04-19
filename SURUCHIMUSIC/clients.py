from pyrogram import Client
from pytgcalls import PyTgCalls
import config

# Bot Client
bot = Client(
    "SURUCHIMUSIC_BOT",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="SURUCHIMUSIC/plugins")
)

# Assistant Client
assistant = Client(
    "SURUCHIMUSIC_ASS",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=config.SESSION_STRING
)

# Music Engine
call = PyTgCalls(assistant)
