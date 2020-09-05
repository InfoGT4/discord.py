import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')
token = open("token.txt","r").readline() # you must have a file called token.txt in the same folder as your .py file

client.run(token)
