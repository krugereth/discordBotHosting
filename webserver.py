from flask import Flask
from threading import Thread
from main import client

app = Flask('')
@app.route('/')
def home():

    return "Discord bot is ok"

def run():
    client.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()