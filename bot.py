import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')

def guild_check(ctx):
    return str(ctx.guild) == "binitagarwal's server" 

bot = commands.Bot(command_prefix='!')

@bot.command(name='basic')
@commands.check(guild_check)
async def hello(ctx,arg):
    if arg.lower() == 'truth':
        print(DISCORD_GUILD)
        send = str(ctx.author) + " You have choosen truth"
        await ctx.send(send)
        print(ctx.guild)


if __name__ == '__main__':
    bot.run(TOKEN)