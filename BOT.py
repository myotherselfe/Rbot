import discord
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
  print("we have loged in as {0.user}".format(client))
 
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  if msg.startswith("#hello"):
    await message.channel.send("hello!")

  if msg.startswith('#sup'):
    await message.channel.send('sup buddy!')

  if msg.startswith("#how are you doing"):
    await message.channel.send("I am doing fine")
  
  if '<@!869747022335451257>' in msg:
    await message.channel.send('{0} DONT EVER PING HIM'.format(message.author.mention))
  
  if msg.startswith("#what are you doing"):
    await message.channel.send("Im doing nothing")
  
  client.run(os.getenv('TOKEN'))

# <@!869747022335451257> MY ID.