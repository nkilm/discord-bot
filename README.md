# Discord Bot

## Steps to make a Discord Bot

- Get TOKEN from [Discord Developer Portal](https://discord.com/developers/applications)
- Start with minimal code(Given Below). 
- Register common events - on_ready, on_message
- client.run(TOKEN) 

## Requirements
![](https://img.shields.io/badge/-discord-%23404eed "pip install discord")
![](https://img.shields.io/badge/-python--dotenv-%23e4d04b "pip install python-dotenv")

## Minimal Code

```python

import discord
from dotenv import load_dotenv 
from os import environ

load_dotenv() # Load the contents of .env file
TOKEN = environ.get('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print("I\'m Up!")

@client.event
async def on_message(msg):

    ''' 

    Do something

    '''
        
client.run(TOKEN)

```