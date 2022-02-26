import discord
from dotenv import load_dotenv 
from os import environ
from requests import get
from random import choice

load_dotenv()

TOKEN = environ.get('ABBOT_TOKEN')


client = discord.Client()

def get_quotes():
  res = get("https://zenquotes.io/api/random")
  quote_info = res.json()[0]
  return f"{quote_info['q']} \n\t- {quote_info['a']}"

def nasa_today():
  try:
    res = get(f"https://api.nasa.gov/planetary/apod?api_key={environ['NASA']}")
    # print(res.json())
    data = res.json()
    return data["title"],data["date"],data["explanation"]
  except:
    return "Error with NASA API(Limit Exceeded)"

  
# registering the events
@client.event
async def on_ready():
    print(f"Logged in {client.user}\n")

@client.event
async def on_message(msg):
  # logging the info
  # print(f"{msg.author}: {msg.content}")

  #actual message from the chat
  message = msg.content
  if msg.author == client.user:
    return

  if (message.startswith("$nasa")):
    title,date,desc = nasa_today()
    await msg.channel.send(f"{date}\n\"{title}\"\n\t{desc}")
  
  if (message.startswith("$info")):
    await msg.channel.send("Available Commands:\n $inspire\t$nasa\t$new\t$del\t$show")

  if message.startswith("$inspire"):
    await msg.channel.send(get_quotes())

client.run(TOKEN)







