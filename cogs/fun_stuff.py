import os
import discord
from discord.ext import commands
from datetime import date
import wolframalpha


app_id = 'T8TJE5-R8HHU3WLQA'
client = wolframalpha.Client(app_id)



def get_difference(date1, date2):
  delta = date2 - date1
  return delta.days


class Fun(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  #date day
  @commands.command()
  async def dating(self, ctx):
    d1 = date(2022, 8, 29)  #start day
    d2 = date.today()  #today
    days = get_difference(d1, d2)
    await ctx.send(f" papa với mama quen nhau được **{days}** ngày rùi đó")

  #wolframalpha
  @commands.command()
  async def ask(self, ctx, *, arg):
    string_result = arg.text

    res = client.query(string_result)
    answer = next(res.results).text

    await ctx.send(answer)

  #find
  @commands.command()
  @commands.guild_only()
  async def find(self, ctx, *, user: discord.Member = None):
     await ctx.send(f'eat ass {user.mention}')
    
async def setup(bot):
  await bot.add_cog(Fun(bot))
