from config import app
import asyncio
import threading, time, requests




if __name__ == "__main__":

    asyncio.run(app.run())
    
    while True:
        try:
            requests.get("https://autopublishing.onrender.com")
        except:
            pass
        time.sleep(600)  # every 10 minutes
