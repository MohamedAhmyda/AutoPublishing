
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

if __name__ == "__main__":
    asyncio.run(app.run())








