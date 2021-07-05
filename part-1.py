import discord
from discord.ext import commands 
client=commands.Bot(command_prefix='>')
@client.event
async def on_ready():
    print('the bot is ready')

@client.command()
async def test2(ctx):
  await ctx.send('hello world')
    @client.command()
async def test(ctx):
    em=discord.Embed(title='hello world',description='welcome to discord.py')
    await ctx.send(embed=em)
    
    
client.run('paste-your-bot-token-here')
