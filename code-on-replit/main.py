import discord
from os import environ
from requests import get
from random import choice
from replit import db
from keep_alive import keep_alive

client = discord.Client()

sad_words =[ 
  "depressing",
  "depressed",
  "sad",
  "unhappy",
  "miserable",
  "unsatisfied"
]

happy_response = [
  "Hang in there. This will get over soon!💯",
  "Cheer Up!💫",
  "Stay strong! you will get through this!😇"
]

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


def update_encouragements(enc_msg):
  # if encouragements key already there in db.keys() then just append
  if ("encouragements" in db.keys()):
    encouragements = db["encouragements"]
    encouragements.append(enc_msg)
    db["encouragements"] = encouragements
  else:
    db['encouragements']= [enc_msg]

def delete_encouragements(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements
  
  
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
  if (message.startswith("$new")):
    new_enc = message.split("$new ")[1]
    update_encouragements(new_enc)
    await msg.channel.send(f"Encouragement \"{new_enc}\" added successfully!")

  if (message.startswith("$show")):
    if ("encouragements" in db.keys()):
      encouragements = db["encouragements"].value
      await msg.channel.send(f"Encouragements {encouragements}")
  if (message.startswith("$nasa")):
    title,date,desc = nasa_today()
    await msg.channel.send(f"{date}\n\"{title}\"\n\t{desc}")
    
  
  if (message.startswith("$del")):
    encouragements = []
    if ("encouragements" in db.keys()):
      index = int(message.split("$del")[1].replace(" ",""))
      delete_encouragements(index)
      await msg.channel.send(db["encouragements"].value)
    else:
      await msg.channel.send(encouragements)
  
  if (message.startswith("$info")):
    await msg.channel.send("Available Commands:\n $inspire\t$nasa\t$new\t$del\t$show")
    
    
  if ("encouragements" in db.keys()):
    global happy_response
    happy_response = happy_response + db["encouragements"].value
                             
  if any((sad_word in message.lower() for sad_word in sad_words)):
    await msg.channel.send(choice(happy_response))
  
  if message.startswith("$inspire"):
    await msg.channel.send(get_quotes())


keep_alive()
client.run(environ['SAMPLE_BOT_TOKEN'])
