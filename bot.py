import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord import colour
from question.truth import file_rand_return
import requests

load_dotenv()

valid_server = ["binitagarwal's server","B-14"] 

TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')

def guild_check(ctx):
    return str(ctx.guild) in valid_server

bot = commands.Bot(command_prefix='!')
bot.add_check(guild_check)
slash = SlashCommand(bot)

@bot.command(name='basic')
async def hello(ctx,arg='truth'):
    if arg.lower() == 'truth':
        embed = discord.Embed(title="Truth",
                            type = "rich",
                            colour=colour.Color(0xe31970)
                            )
        author = ctx.author
        question = file_rand_return()
        embed.add_field(name=f"{question}",value=f'{author}',inline=False)
        embed.set_footer(text="Made with ❤️ by Nittishna and Binit")
        await ctx.send(embed=embed)

@slash.slash(name='hello')
async def slashHello(ctx:SlashContext):
    embed = discord.Embed(title="embed test")
    value = str(ctx.author) + " You have choosen truth"
    await ctx.send(content=f"{value}", embeds=[embed])


if __name__ == '__main__':
    bot.run(TOKEN)