import os
from datetime import datetime

# --- Bot Credentials ---
API_ID = 39005479
API_HASH = "c2e7265b2e96025adcc4731c2c1e5ba5"
BOT_TOKEN = "8357466207:AAGNJy4DYDSFSHPZ8fELwsuvfU3l0indKkE"
SESSION_STRING = "BQE-4i0ATBa04O65GCMroeZlZa8aJP2tUFcHVxM5DNsnf3HvO0K4E7Zy8zFYHVhYutVtSInbU3oZIJaULAMNPlfLKhidwjgOZZ2HcmJKhKgAB78RRMQcFsrdOcDiPeCzzzScLWlNs5ccxiw3Nmju0hcLmIvrxTXwLkATiUU058mRT0W9i0AT19PHx--E-VScSyaiDxHe1vC1SBcOp8zcGmNX0LUt3kWzxtx2uOdMmYu3ArI5UqGNmSbw9yvtii4YaKYL6xzSX_BhtSN4TWHa0-fgK9e46xtqsDrMtMWI7ZHNN5gkFmxhDpvOt5V_R0arZ12bQEkfIXeb6u1t1PCtEaoPJCD-swAAAAHKarFXAA"
# --- Random image links ---" # Apni session string yahan puri daal dena
OWNER_ID = 8762528787
# --- Global Tracking ---
queues = {}
playing_messages = {} # {chat_id: message_id} - Timer edit karne ke liye
current_playing = {} # {chat_id: song_details} - Currently playing track ke liye
BOT_START_TIME = datetime.now()
