import discord
import os
import secrets

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
      await message.channel.send(secrets.SystemRandom().choice(file.readlines()))
client.run('tokenhere')

