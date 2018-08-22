import discord
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix = "")

@client.event
async def on_ready():
    print("The bot is online!")

@client.event
async def on_message(message):
    if message.content == "!hello":
        await client.send_message(message.author, "Hello World!")
    if message.content == "Help":
        await client.send_message(message.author, "Help Info\n\nCommands:\n!hello - ValBot will DM you \"Hello World\"")

client.run("NDgxODA5NzM2MTcwNDcxNDI0.Dl7wtg.bHuL_lcde_kEavWR2d2cVD9FmFw")
