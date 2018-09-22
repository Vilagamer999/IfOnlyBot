import discord
import os
import sys
import random
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print(client.user, "is ready!")
    await client.change_presence(game=discord.Game(name='/g join IfOnly'))

@client.event
async def on_message(message):
    if message.author != client.user:
	    if message.content.startswith('!help'):
		    await client.add_reaction(message, "😄")
		    tmp = await client.send_message(message.channel, '***IfOnly bot help menu:***\n```\n!help - Displays this help menu.\n\n!about - Displays info about the bot.\n\n!debug - Add an argument to run debug commands (for developers of bot).\n\n!random - Generates a random number between 1 and 500000.\n\n!apply - Get the guild application\n\n!server - Get an invite to the IfOnly guild Discord server!\n```')
	    elif message.content.startswith('!about'):
		    tmp = await client.send_message(message.channel, '*Hello, I am IfOnly#1538, better known as the IfOnly bot.  I am developed by jumbocakeyumyum for the IfOnly Hypixel guild.  I am still in testing, and you should let my creator know if you find any bugs.*') 
	    elif message.content.startswith('!apply'):
	        tmp = await client.send_message(message.channel, "**Guild application:**\nIn-Game Name (IGN):\nRank (On Hypixel):\nDo you like cheese?:\nWhat is your total # of SkyWars and or BedWars wins?:\nWhat is your network level on Hypixel?:\nWhich guild role are you applying for?:\nHow active would you say you are?:\n")
	    elif message.content.startswith('!server'):
	        await client.create_invite(message.channel)
	        tmp = await client.send_message(message.channel, 'https://discord.gg/DmAqWfQ')
	    elif message.content.startswith('!random'):
		    tmp = await client.send_message(message.channel, "Your random number is:")
		    tmp = await client.send_message(message.channel, random.randint(1, 500000))
	    elif message.content.startswith('!debug check'):
		    tmp = await client.send_message(message.channel, ":white_check_mark: I'm online!")
	    elif message.content.startswith('!debug stop'):
		    await client.add_reaction(message, "☣")
		    await client.add_reaction(message, "😦")
		    tmp = await client.send_message(message.channel, '***Bot now shutting down.  Please ignore any errors in the console.***')
		    sys.exit("Detected a !debug.stop request")
	    elif message.content.startswith('!serverinfo'):
		    tmp = await client.send_message(message.channel, 'Coming soon')

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
