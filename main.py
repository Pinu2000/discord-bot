# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD') 

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

 


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content.lower() == '!hello':
        response = ("I can understand that! ")
        await message.channel.send(response)
        



    if message.content.lower() == ('!rick'):
        response = ("https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713")
        await message.channel.send(response)
        
    if message.content.lower() == '!bye':
        response = ("빠이ㅣㅣ")
        await message.channel.send(response)

    if message.content.lower() == ('!help'): 
        response = ("Commands-->   !hello, !bye, !rick, !smpip")
        await message.channel.send(response)
        
    if message.content.lower() ==('!smpip'):
        response = ("/join SMPv2PinGu.minehut.gg")
        await message.channel.send(response)

client.run(TOKEN)