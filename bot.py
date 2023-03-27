import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True 
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send('pong')
    await ctx.send(f'Hi {ctx.author.mention}!')

client.run('MTA4OTc5Njc3MjMwMzQ3NDc5OQ.GXL-Cx.FaMB0C-Oi1UdeOjxP2UyR2MK-MWF5iipMhnR2k')
