from config import app
import asyncio
import threading, time, requests

@app.route('/')
def home():
    return "I'm alive"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

def ping_self():
    while True:
        try:
            requests.get("https://autopublishing.onrender.com")
        except:
            pass
        time.sleep(600)  # every 10 minutes

# Start Flask server + keep-alive pinger
threading.Thread(target=run_flask, daemon=True).start()
threading.Thread(target=ping_self, daemon=True).start()


if __name__ == "__main__":

    asyncio.run(app.run())
    

