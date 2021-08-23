import discord
import os
# import random
from dotenv import load_dotenv
from discord.ext import commands
# from discord_slash import SlashCommand, SlashContext
from discord import colour
from question.truth import file_rand_return
from question.dare import file_rand_return_dare
 
load_dotenv()


TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')

def guild_check(ctx):
    return (str(ctx.message.guild.id) in valid_server_id)

bot = commands.Bot(command_prefix='!')
bot.add_check(guild_check)
# slash = SlashCommand(bot)

@bot.command(name='basic')
async def hello(ctx,arg="random"):
    if arg.lower() == 'truth':
        embed = discord.Embed(title="Truth",
                            type = "rich",
                            colour=colour.Color(0xe31970)
                            )
        author = ctx.author
        question = file_rand_return()
        embed.add_field(name=f"{question}",value=f'{author}',inline=False)
        embed.set_footer(text="Made with ❤️ by basic and Binit")
        await ctx.send(embed=embed)
        return
    
    elif arg.lower() == 'dare':
        embed = discord.Embed(title="Dare",
                            type = "rich",
                            colour=colour.Color(0xe31970)
                            )
        author = ctx.author
        question = file_rand_return_dare()
        embed.add_field(name=f"{question}",value=f'{author}',inline=False)
        embed.set_footer(text="Made with ❤️ by basic and Binit")
        await ctx.send(embed=embed)
        return

    else:
        embed = discord.Embed(title="ERROR",
                            type = "rich",
                            colour=colour.Color(0xf70566)
                            )
        author = ctx.author
        embed.add_field(name=f"Kindly add Truth or Dare",value=f'{author}',inline=False)
        embed.set_footer(text="Made with ❤️ by basic and Binit")
        await ctx.send(embed=embed)
        return


# @slash.slash(name='hello')
# async def slashHello(ctx:SlashContext):
#     embed = discord.Embed(title="embed test")
#     value = str(ctx.author) + " You have choosen truth"
#     await ctx.send(content=f"{value}", embeds=[embed])


if __name__ == '__main__':
    bot.run(TOKEN)
