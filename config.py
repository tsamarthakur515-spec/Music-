import os
from datetime import datetime

# --- Bot Credentials ---
API_ID = 39005479
API_HASH = "c2e7265b2e96025adcc4731c2c1e5ba5"
BOT_TOKEN = "8596765113:AAGlK4eW_0Qxlt6hfD_ElFcwronZivnNM6w"
SESSION_STRING = "BQE-4i0AclIM1MxvSfSiIlXqBAZNJttV9NpXiIjzKpNtQ-7iwCF_UtL_PeeTIWlVtyJJiJDbPP8AMxLiTf8HQcXhYl1D8e1fiLdJB6VSZpdnbLSfVUjGs_8px-rhz0Ql99f1EiEjcFcgUbQtTuwaw_XSHPMbxV-_z69F7XzrmN9Z0kQKEljA6O7YTn2TfnjF9wIWICWmnP2I9AVybQmhDvKDEge_6GY7e0a59qVXaLHRFMj3iUTt9ca0ldOg43J5NHakn0pFXkqyuGXvM60hubcynP7WXCLOiuc1Ct0GD3gjBxRS6EtNtccWK8EpksJCCC70dIb7vp_Y5l0u1eZ2JjVkGyPyagAAAAH-nwzIAA"
# --- Random image links ---" # Apni session string yahan puri daal dena
OWNER_ID = 8566803656
# --- Global Tracking ---
queues = {}
playing_messages = {} # {chat_id: message_id} - Timer edit karne ke liye
current_playing = {} # {chat_id: song_details} - Currently playing track ke liye
BOT_START_TIME = datetime.now()
