# bot.0.1.py
# Helpful links: https://discordpy.readthedocs.io/en/stable/api.html#messages
import os
import os.path
import sys
import discord
import asyncio  # Timer
from dotenv import load_dotenv
from discord.ext import tasks
from discord.ext import commands
from discord.ext.commands import CommandNotFound # Get rid of 'discord.ext.commands.errors.CommandNotFound:' error


# Info / Sites / Tips
# Instagram: https://www.instagramez.com/reel/DD1t-BpIIe-/?igsh=YXpudmx5cHhlazNw
# Instagram: https://www.ddinstagram.com/reel/DBm8GYASueQ/?igsh=YzljYTk1ODg3Zg==
# X:         https://fxtwitter.com/YouFuckingIdio9/status/1871077024783122796
# Reddit:    https://www.rxddit.com/r/DataHoarder/s/it2HXGW55l
# YT:        https://www.yout-ube.com/watch?v=Uy1F3PV9YXM  (NO EMBED)       
# YT:        https://koutu.be
# TikTok:    https://tnktok.com


load_dotenv()
description = '''
God, this is annoying as all hell.
Fuck Python in it's stupid magical ass.
'''

TOKEN = os.getenv('DISCORD_TOKEN')  # BOT Token
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(description=description, command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
 #   print(f"Invite link: https://discordapp.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8")
    print('------')

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot: # Let's not respond to ourselves.
         return
    if "https://x.com/" in message.content:
        new_message = message.content.replace("x.com", "fxtwitter.com")
        new_message = message.author.display_name + " Posted " + new_message
        await message.channel.send(new_message)
        await message.delete()
    if "https://www.instagram.com/" in message.content:
        new_message = message.content.replace("instagram.com/", "instagramez.com/")
        new_message = message.author.display_name + " Posted " + new_message
        await message.channel.send(new_message)
        await message.delete()        
    if "https://www.reddit.com/" in message.content:
        new_message = message.content.replace("reddit.com/", "rxddit.com/")
        new_message = message.author.display_name + " Posted " + new_message
        await message.channel.send(new_message)
        await message.delete()      
    if "https://www.youtube.com/w" in message.content:
        new_message = message.content.replace("www.youtube.com/", "koutu.be/view/")
        new_message = message.author.display_name + " Posted " + new_message
        await message.channel.send(new_message)
#        await message.delete() # Let's not delete the MSG yet
    if "https://youtu.be/" in message.content:
        new_message = message.content.replace("youtu.be/", "koutu.be/view/")
        new_message = message.author.display_name + " Posted " + new_message
        await message.channel.send(new_message)
#        await message.delete()
#   tnktok.com
    if "https://www.tiktok.com/" in message.content:
        new_message = message.content.replace("tiktok.com/", "tnktok.com/")
        new_message = message.author.display_name + " Posted " + new_message
        await message.channel.send(new_message)
        await message.delete()   
    await bot.process_commands(message)

@bot.command(name="ping",
             help="Test the bots responsiveness.",
             brief="Is the bot alive? ... am I alive?")
async def ping_pong(ctx):
	await ctx.channel.send("pong")


## 
# TESTING AREA
##

@bot.command(name="Embed",
             help="Just for Testing",
             brief="Tests the embed command while I code it")
async def embed(ctx):
    embed = discord.Embed(title="LazyB Bot", description="Your Link") #,color=Hex code
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.add_field(name="Name", value="you can make as much as fields you like to")
    await ctx.send(embed=embed)

# For Embeds -- No Workie, needs webhooks
"""
@bot.event
async def on_message(message: discord.Message):
    if message.author.bot: # Let's not respond to ourselves.
         return
    if "https://x.com/" in message.content:
        new_message = message.content.replace("x.com", "fxtwitter.com")
        await message.channel.send(new_message)
        await message.delete()
    if "https://www.instagram.com/reel" in message.content:
        new_message = message.content.replace("instagram.com/", "instagramez.com/")
        embed = discord.Embed(title="Posted", description=new_message) #,color=Hex code
        embed.set_author(name=message.author.display_name, icon_url=message.author.avatar)
        await message.channel.send(embed=embed)
        await message.delete()        
    await bot.process_commands(message)
"""
# NO NEED TO EDIT PAST THIS LINE
# Remove 'discord.ext.commands.errors.CommandNotFound: Command' from terminal window. 
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):  # Using `==` is incorrect
        return
    raise error

bot.run(TOKEN)