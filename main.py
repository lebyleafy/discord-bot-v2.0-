import discord
import os
from online import keep_alive
import asyncio
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import rep
import random

intents = discord.Intents().all()
intents.members = True
commands = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                        intents=intents,
                        help_command=None)


#bot notice message

#load feature
async def load():
  for file in os.listdir('./cogs'):
    if file.endswith('.py'):
      await commands.load_extension(f'cogs.{file[:-3]}')


#commands doesnt exist
@commands.event
async def on_command_error(ctx, error):
  if isinstance(error, CommandNotFound):
    await ctx.send("lol no, that command doesn't even exist")


#bot activity
@commands.event
async def on_ready():
  print('We have logged in as {0.user}'.format(commands))
  await commands.change_presence(
    status=discord.Status.idle,
    activity=discord.Streaming(
      name=f"in {len(commands.guilds)} servers",
      url='https://www.youtube.com/watch?v=DaEjIcSQbpk'))


#load token and feature
async def main():
  await load()
  await commands.start(os.getenv('TOKEN'))


asyncio.run(main())
keep_alive()
