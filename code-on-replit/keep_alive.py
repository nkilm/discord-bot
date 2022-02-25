from flask import Flask
from threading import Thread

app = Flask('')

@app.route("/")
def home():
  return "Hey There! I\'m still Up:)"

def run():
  app.run(host='0.0.0.0', port = 7070)

def keep_alive():
  t = Thread(target=run)
  t.start()