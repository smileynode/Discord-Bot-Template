import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("Bot Is Currently Online.")

client.run('your token here')
