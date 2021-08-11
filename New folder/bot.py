import discord
import os
import random
client = discord.Client()

@client.event
async def on_ready():
  print('We have loggon in as {0.user}'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  

  if message.content.startswith('$wisdom'):
    with open('./resources/file.txt', 'r', encoding="utf8") as file:
      await message.channel.send(random.choice(file.readlines()))
client.run('tokenhere')

