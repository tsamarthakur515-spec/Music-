import asyncio
from pyrogram import idle, Client
from SURUCHIXMUSIC.clients import bot, assistant, call 
import config

async def start_bot():
    print("🚀 Starting SURUCHIMUSIC Clients...")
    
    # --- PLUGINS LOADING LOGIC ---
    # Ye batata hai bot ko ki commands kahan rakhi hain
    bot.plugins = {"root": "SURUCHIMUSIC/plugins"} 
    
    await bot.start()
    await assistant.start()
    await call.start()
    
    print("---------------------------------")
    print("✨ SURUCHIMUSIC IS NOW ONLINE! ✨")
    print("✅ ALL MODULES LOADED")
    print("---------------------------------")
    
    await idle()
    
    # Stopping clients on exit
    await bot.stop()
    await assistant.stop()
    await call.stop()

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(start_bot())
    except KeyboardInterrupt:
        print("\n🛑 Bot Stopped.")
