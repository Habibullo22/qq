# keep_alive.py
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot tirik!"

def keep_alive():
    t = Thread(target=lambda: app.run(host='0.0.0.0', port=8080))
    t.start()

if __name__ == "__main__":
    keep_alive()  # faqat fayl bevosita ishga tushirilsa ishlaydi
if __name__ == "__main__":
    keep_alive()
