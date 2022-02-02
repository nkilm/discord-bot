from dotenv import load_dotenv 
from os import environ
import discord

load_dotenv()

TOKEN = environ.get('TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f"Logged in - {client.user}")
    # print("Logged in - {0.user}".format(client))
    # print(client.user)

@client.event
async def handle_msg(msg_obj):
    username = str(msg_obj.author).split("#")[0]
    msg = str(msg_obj.content)
    channel = str(msg_obj.channel.name)
    print(f"{username} : {msg} : ({channel}) ")

    # to prevent the bot from replying to itself 
    if msg_obj.author == client.user:
        return 
    
    if msg_obj.channel.name == "Testing Server for bots":
        if msg.lower() == "hello":
            await msg_obj.channel.send(f"Hello {username}")
            return 
        
client.run(TOKEN)







