from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return"Hello. I am alive!"

def run():
  app.run(host = '0.0.0.0',port = 8080)

def run_forever():
    t = Thread(target=run)
    t.start()

		# embedve.add_field(name=Server Count, value=f"Server Count - ( int(len (list(client.guilds)))servers", inline = False)