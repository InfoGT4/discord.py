import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')
client.remove_command("help")
token = open("token.txt","r").readline()

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}!")
    print("-----------------")
    await client.change_presence(activity=discord.Game(name=f"Hello, my name is {client.user.name} and I will help you!\n!help"))

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send(f"Hey {member.mention}, Welcome to this test server!")
    print(f"{member} join the server!")
  
client.run(token)
