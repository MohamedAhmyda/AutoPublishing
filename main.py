
from config import app
import asyncio
import threading, time, requests
import logging
from flask import Flask

# ---------- SETUP LOGGING ----------
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# ---------- FLASK KEEP-ALIVE ----------
app = Flask(__name__)

@app.route('/')
def home():
    logging.info("Render / home endpoint was pinged.")
    return "I'm alive"

def run_flask():
    logging.info("Starting Flask server for keep-alive...")
    app.run(host="0.0.0.0", port=10000)

def ping_self():
    url = "https://your-service-name.onrender.com"  # Replace with your Render URL
    while True:
        try:
            requests.get(url)
            logging.info(f"Pinged self successfully: {url}")
        except Exception as e:
            logging.error(f"Error pinging self: {e}")
        time.sleep(600)  # every 10 minutes

# ---------- TELEGRAM BOT EXAMPLE ----------
def run_bot():
    logging.info("Starting Telegram bot...")
    # Example Telethon bot code
    # from telethon import TelegramClient
    # client = TelegramClient("session", api_id, api_hash)
    # client.start()
    # client.run_until_disconnected()
    while True:
        logging.info("Bot is running...")
        time.sleep(300)  # simulate bot running

# ---------- START THREADS ----------
threading.Thread(target=run_flask, daemon=True).start()
threading.Thread(target=ping_self, daemon=True).start()
threading.Thread(target=run_bot, daemon=True).start()

# Keep main thread alive
while True:
    time.sleep(600)

if __name__ == "__main__":

    asyncio.run(app.run())
    





