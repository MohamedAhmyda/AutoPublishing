
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

# ---------- FLASK KEEP-ALIVE ----------
server = Flask(__name__)

@server.route('/')
def home():
    logging.info("HTTP / request received — service is alive.")
    return "✅ Pyrogram bot is alive and responding!"

def run_server():
    logging.info("Starting Flask keep-alive server on port 10000...")
    server.run(host="0.0.0.0", port=10000)

# ---------- PING SELF ----------
def ping_self():
    url = "https://your-service-name.onrender.com"  # <-- replace with your actual Render URL
    while True:
        try:
            r = requests.get(url)
            if r.status_code == 200:
                logging.info(f"[PING] Successful self-ping: {url}")
            else:
                logging.warning(f"[PING] Unexpected status code: {r.status_code}")
        except Exception as e:
            logging.error(f"[PING] Failed to ping self: {e}")
        time.sleep(600)  # ping every 10 minutes

# ---------- RUN BOT ----------
async def main():
    logging.info("Starting Pyrogram bot and keep-alive threads...")

    # Start Flask server (thread)
    threading.Thread(target=run_server, daemon=True).start()

    # Start self-ping thread
    threading.Thread(target=ping_self, daemon=True).start()

    # Start Pyrogram bot
    logging.info("Launching Pyrogram bot...")
    await app.run()  # your bot from config.py

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    logging.info("Initializing main event loop...")
    asyncio.run(main())






