
from config import app
import asyncio
import threading, time, requests
import logging
from flask import Flask


# ---------- LOGGING SETUP ----------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
import asyncio
import threading
import time
import requests
import logging
from flask import Flask
from pyrogram import idle
from config import app  # بوتك من config.py

# ---------- LOGGING ----------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# ---------- FLASK ----------
server = Flask(__name__)

@server.route('/')
def home():
    logging.info("✅ / endpoint was pinged")
    return "Pyrogram bot is alive and Flask running."

def run_server():
    logging.info("🚀 Starting Flask server on port 10000...")
    server.run(host="0.0.0.0", port=10000)

# ---------- SELF PING ----------
def ping_self():
    url = "https://autopublishing.onrender.com"  # ← حط رابط Render هنا
    while True:
        try:
            requests.get(url)
            logging.info(f"[PING] Successful self-ping to {url}")
        except Exception as e:
            logging.error(f"[PING] Failed: {e}")
        time.sleep(600)  # كل 10 دقايق

# ---------- BOT ----------
async def run_bot():
    try:
        logging.info("🤖 Starting Pyrogram bot...")
        await app.start()
        me = await app.get_me()
        logging.info(f"✅ Logged in as: {me.first_name} (@{me.username})")
        await idle()  # keeps it running
    except Exception as e:
        logging.error(f"❌ Error running bot: {e}")
    finally:
        await app.stop()
        logging.info("🛑 Bot stopped.")

# ---------- MAIN ----------
async def main():
    # Run Flask in separate thread
    threading.Thread(target=run_server, daemon=True).start()
    # Run keep-alive pinger
    threading.Thread(target=ping_self, daemon=True).start()
    # Run the bot
    await run_bot()

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
