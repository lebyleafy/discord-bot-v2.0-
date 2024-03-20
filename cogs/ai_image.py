import os
import discord
from discord.ext import commands
import openai

openai.api_key = os.getenv('OPENAI_TOKEN')

class ai_image(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def generate(self, ctx: commands.Context, *, arg):
    prompting = await ctx.send(f"Generating prompt \"{arg}\"...")
  
    response = openai.images.generate(
    prompt= arg,
    size="1024x1024",
    quality="standard",
    n=1,)
    
    image_url = response.data[0].url
    await ctx.reply(image_url)
    await prompting.delete()

async def setup(bot):
  await bot.add_cog(ai_image(bot))
