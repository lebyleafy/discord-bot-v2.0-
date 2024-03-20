from discord import Intents
from discord.ext import commands
from discord.ext import menus
from discord.ext.menus import button, First, Last
import discord


class MyMenuPages(menus.MenuPages, inherit_buttons=False):
  @button('<:before_fast_check:754948796139569224>', position=First(0))
  async def go_to_first_page(self, payload):
      await self.show_page(0)

  @button('<:before_check:754948796487565332>', position=First(1))
  async def go_to_previous_page(self, payload):
      await self.show_checked_page(self.current_page - 1)

  @button('<:next_check:754948796361736213>', position=Last(1))
  async def go_to_next_page(self, payload):
      await self.show_checked_page(self.current_page + 1)

  @button('<:next_fast_check:754948796391227442>', position=Last(2))
  async def go_to_last_page(self, payload):
      max_pages = self._source.get_max_pages()
      last_page = max(max_pages - 1, 0)
      await self.show_page(last_page)

  @button('<:stop_check:754948796365930517>', position=Last(0))
  async def stop_pages(self, payload):
      self.stop()


class MySource(menus.ListPageSource):
  async def format_page(self, menu, entries):
    embed = discord.Embed(
      title='How to use mr Monkey',
      description=
      'page 1/5',
      color=0x774dea)
    embed.set_author(
      name="Monkey",
      url=
    "https://discord.com/oauth2/authorize?client_id=1217842566452609145&permissions=8&scope=bot",
      icon_url=
    "hhttps://cdn.discordapp.com/attachments/826292876207849493/1218059503459635251/Monkey-Selfie.jpg-2.png?ex=66064950&is=65f3d450&hm=3aafef89bc81a9d0d485d06e58d69d2bc87c4ce949c9c6e998b412d65a3586d5&"
  )
    embed.set_thumbnail(url=
    "https://media2.giphy.com/media/p2ogddPRRwie0Vbxnz/giphy.gif?cid=6c09b952on5mf08uuim5setuxeko9widkinjtdj9oykzg68z&ep=v1_stickers_related&rid=giphy.gif&ct=ts"
  )
    embed.add_field(name="Slot machine 🎰", value="slot/slots/sl **{ammount}**")
    embed.add_field(name="Coinflip 🪙",
                  value="coinflip/coim_flip/cf {head/tail} **{ammount}**")
    embed.add_field(name="Dice 🎲",
                  value="rolldice/roll_dice/rd/rdice **{ammount}**",
                  inline=False)
    embed.add_field(name="Slavery 👨‍💻", value="work")
    embed.add_field(name="Daily/weekly reward 💵", value="daily & weekly")
    embed.add_field(name="Money you have 💳",
                  value="balance/bal/money/bank",
                  inline=False)
    embed.add_field(
      name="Deposit/Withdraw money from bank 🏦",
      value=f"**deposit**: deposit/dep/ds \n **withdraw**: withdraw/wd/widr")
    embed.add_field(name="Beggar fr 🤲 ", value="beg")
    embed.add_field(name="Robbery fr 💸 ",
                  value="rob ***{@mention}***")
    embed.add_field(name="Send someone money 💱",
                  value="give ***{@mention}*** **{ammount}**")
    embed.add_field(name="Jail someone 👮",
                  value="jail ***{@nmention}***")
    embed.add_field(name="Free someone from jail 🕊",
                  value="release ***{mention}***")
    embed.add_field(name="Solve math 🖩", 
                  value="math **{question}**")
    embed.add_field(name="Ask anything❓", 
                  value="ask **{question}**")
    embed.add_field(name="AI Image 🖼️", value="generate **{prompt}**")
    embed.set_footer(
      text="contact to author if you have any question or suggestion")


    embed2 = discord.Embed(
      title='How to use mr Monkey',
      description=
      'page 2/5',
      color=0x774dea)
    embed2.set_author(
      name="Monkey",
      url=
    "https://discord.com/oauth2/authorize?client_id=1217842566452609145&permissions=8&scope=bot",
      icon_url=
    "hhttps://cdn.discordapp.com/attachments/826292876207849493/1218059503459635251/Monkey-Selfie.jpg-2.png?ex=66064950&is=65f3d450&hm=3aafef89bc81a9d0d485d06e58d69d2bc87c4ce949c9c6e998b412d65a3586d5&"
  )
    embed2.set_thumbnail(url=
    "https://media2.giphy.com/media/p2ogddPRRwie0Vbxnz/giphy.gif?cid=6c09b952on5mf08uuim5setuxeko9widkinjtdj9oykzg68z&ep=v1_stickers_related&rid=giphy.gif&ct=ts"
  )
    embed2.add_field(name="Mathematic graphing", 
                     value="linear/parabola/cubic ")
    embed2.add_field(name="Encrypt/Decrypt 💻",
                     value=
  "``!encrypt <keywords>``, convert string to morse. ``!decrypt <morse code>`` convert morse to string"
)
    embed2.add_field(name="Hex to text/text to hex",
                     value=
  "``!texttohex <keywords>``, convert string to hexadecimal. ``!hextotex <hex code>`` convert hex to string"
)
    embed2.add_field(name="Binary to text/text to binary",
                     value=
  "``!texttobinary <keywords>``, convert string to binary. ``!binarytotext <binary>`` convert binary to string"
)
    embed2.add_field(name="Mock text",
                    value="``Mock <value>``to reverse text")
    embed2.add_field(name="Reverse text",
                     value="dias uoy tahw esrever")
    embed2.add_field(name="Flip text",
                     value="pǝddᴉꞁɟ sᴉ sᴉɥ⊥")
    embed2.add_field(name="Purge message",
                     value="``!purge <value>``")
    embed2.add_field(name="Rock paper scissors :fist: :v: :raised_hand: ",
                     value="``!rps <rock, paper, scissors>`` to play rock-paper-scissors")
    embed2.add_field(name="Minesweeper 💣",
                     value="Play minesweeper")
    embed2.add_field(name="Fun image",
                     value="``shit {value}``,``achievement {value}``, ``trash {user mention}``, ``wanted {user mention}``,``pixel {user mention}``,``ascii {user mention}``")
    embed2.set_footer(text="contact to author if you have any question or suggestion")

    
    if entries == 1: 
        return embed
    elif entries == 2:
        return embed2
    else: 
        pass
      
  
class Help(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def help(self, ctx):
    data = [1, 2, 3, 4, 5]
    formatter = MySource(data, per_page=1)
    menu = menus.MenuPages(formatter)
    await menu.start(ctx)
    await interaction.response.send_message(view=MySource()) 
  

async def setup(bot):
  await bot.add_cog(Help(bot))
