import matplotlib.pyplot as plt
import numpy as np
import os
import discord
from discord.ext import commands
from datetime import date
from math import *
import wolframalpha


app_id = 'T8TJE5-R8HHU3WLQA'
client = wolframalpha.Client(app_id)


class math_fun(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  #parabola
  @commands.command()
  @commands.guild_only()
  async def parabola(self, ctx, a: int, b: int, c: int):
      x = np.linspace(-10, 10, 1000)
      fig, ax = plt.subplots()
      y = a * x**2 + b * x + c
      ax.plot(x, y, 'g', label=f'y={a}x²+{b}x+{c}')
      plt.legend(loc='upper left')

      plt.grid()
      plt.savefig("foo.png")
      await ctx.send(file=discord.File("foo.png"))
      os.remove("foo.png")


  #linear
  @commands.command()
  @commands.guild_only()
  async def linear(self, ctx, a: int, b: int):
      fig = plt.figure()
      ax = fig.add_subplot(1, 1, 1)
      x = np.linspace(-5, 5, 100)
      ax.spines['left'].set_position('center')
      ax.spines['bottom'].set_position('center')
      ax.spines['right'].set_color('none')
      ax.spines['top'].set_color('none')
      ax.xaxis.set_ticks_position('bottom')
      ax.yaxis.set_ticks_position('left')
      plt.plot(x, a * x + b, '-r', label=f"y={a}x+{b}")
      plt.legend(loc='upper left')

      plt.grid()
      plt.savefig("foo2.png")
      await ctx.send(file=discord.File("foo2.png"))
      os.remove("foo2.png")


  #cubic
  @commands.command()
  @commands.guild_only()
  async def cubic(self, ctx, a: int):
        x = np.linspace(-np.pi, np.pi, 100)
        y = np.sin(x)
        z = np.cos(x)

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x, y * a, 'c', label=f'y={a}sin(x)')
        plt.plot(x, z * a, 'm', label=f'y={a}cos(x)')
        plt.legend(loc='upper left')

        plt.grid()
        plt.savefig("foo3.png")
        await ctx.send(file=discord.File("foo3.png"))
        os.remove("foo3.png")




  #do math
  @commands.command()
  async def math(self, ctx, *, arg):

      res = client.query(arg)
      answer = next(res.results).text

      await ctx.send(answer)

async def setup(bot):
  await bot.add_cog(math_fun(bot))