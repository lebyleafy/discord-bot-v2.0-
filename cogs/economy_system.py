import discord
import os
import random
from online import keep_alive
from discord.ext import commands
import asyncio
import json
import math
from discord.ext.commands import cooldown, BucketType
import time
from discord.utils import get

with open("bank.json", "ab+") as ab:
  ab.close()
  f = open('bank.json', 'r+')
  f.readline()
  if os.stat("bank.json").st_size == 0:
    f.write("{}")
    f.close()
  else:
    pass


async def open_account(user):
  users = await get_bank_data()

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["Wallet"] = 0
    users[str(user.id)]["Bank"] = 0

  with open("bank.json", 'w') as f:
    json.dump(users, f)

  return True


async def get_bank_data():
  with open("bank.json", 'r') as f:
    users = json.load(f)
  return users


async def update_bank(user, change=0, mode="Wallet"):
  users = await get_bank_data()
  users[str(user.id)][mode] += change
  with open("bank.json", "w") as f:
    json.dump(users, f)
  bal = [users[str(user.id)]["Wallet"], users[str(user.id)]["Bank"]]
  return bal


class Economy(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
#jail

  @commands.command(pass_context=True)
  @commands.has_role('Government')
  @commands.guild_only()
  async def jail(self, ctx, *, member: discord.Member = None):
    if member is None:
      await ctx.send("choose someone to jail")

    role = get(member.guild.roles, name="jailed")
    await member.add_roles(role)
    await ctx.send(f"**{member.mention}** jailed")

#relase

  @commands.command(pass_context=True)
  @commands.has_role('Government')
  @commands.guild_only()
  async def release(self, ctx, member: discord.Member):
    if member is None:
      await ctx.send("Who u wanna release?")

    role = get(member.guild.roles, name="jailed")
    await member.remove_roles(role)
    await ctx.send(f"**{member.mention}** don't commit crime again dumbass")

#withdraw money

  @commands.command(name="withdraw", aliases=["wd", 'widr'])
  @commands.guild_only()
  async def withdrawmoney(self, ctx, amount: str = None):
    if amount is None:
      await ctx.send("How much u want")
      return
    bal = await update_bank(ctx.author)
    if amount.lower() in "all":
      await ctx.send("wut?")

    if int(amount) > bal[1]:
      await ctx.send("u broke lmao")
      return
    if int(amount) < 0:
      await ctx.send("huh?")
      return
    if int(amount) > 0:
      amount = int(amount)
      await update_bank(ctx.author, amount)
      await update_bank(ctx.author, -1 * amount, "Bank")
      await ctx.send(f"mr Monkey giving **{amount}** coins for {ctx.author.mention}")

#deposit money

  @commands.command(name="deposit", aliases=["ds", "dep"])
  @commands.guild_only()
  async def depositmoney(self, ctx, amount: str = None):
    if amount is None:
      await ctx.send(f"{ctx.author.mention} how much u want to deposit man")
      return
    bal = await update_bank(ctx.author)
    if amount.lower() in ["max", "all"]:
      await update_bank(ctx.author, -1 * bal[0])
      await update_bank(ctx.author, bal[0], "Bank")
      await ctx.send(f"already lil bro")

    if int(amount) > bal[0]:
      await ctx.send("not enough u poor bitch")
      return

    if int(amount) < 0:
      await ctx.send("damn bro what?")
      return

    if int(amount) > 0:
      amount = int(amount)
      await update_bank(ctx.author, -1 * amount)
      await update_bank(ctx.author, amount, "Bank")

      await ctx.send(f'mr Monkey deposited **{amount}** coins into the bank')

#check money

  @commands.command(name="balance", aliases=["bal", "money", 'bank'])
  @commands.guild_only()
  async def balance(self, ctx):
    await open_account(ctx.author)

    user = ctx.author
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["Wallet"]
    bank_amt = users[str(user.id)]["Bank"]

    em = discord.Embed(title=f"{ctx.author.name}'s balance.",
                       color=discord.Color.teal())
    em.add_field(name="Wallet Balance", value=wallet_amt)
    em.add_field(name="Bank Balance", value=bank_amt)
    await ctx.send(embed=em)

#beg for money

  @commands.command()
  @commands.cooldown(1, 18000, commands.BucketType.user)
  @commands.guild_only()
  async def beg(self, ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(50)

    await ctx.send(
      f"some rich guy donated to **{ctx.author.mention}** ***{earnings}*** coins")

    users[str(user.id)]["Wallet"] += earnings

    with open("bank.json", 'w') as f:
      json.dump(users, f)

#daily money

  @commands.command()
  @commands.cooldown(1, 86400, commands.BucketType.user)
  @commands.guild_only()
  async def daily(self, ctx):

    await open_account(ctx.author)

    user = ctx.author

    role = discord.utils.find(lambda r: r.name == 'jailed',
                              ctx.message.guild.roles)

    if role in user.roles:
      await ctx.send("nah bro".format(user))
    else:
      users = await get_bank_data()

      earnings = random.randrange(150, 300)

      await ctx.send(
        f"{ctx.author.mention} earned **{earnings}** coins")

      users[str(user.id)]["Wallet"] += earnings

      with open("bank.json", 'w') as f:
        json.dump(users, f)
#weekly money

  @commands.command()
  @commands.cooldown(1, 604800, commands.BucketType.user)
  @commands.guild_only()
  async def weekly(self, ctx):
    await open_account(ctx.author)

    user = ctx.author

    role = discord.utils.find(lambda r: r.name == 'jailed',
                              ctx.message.guild.roles)

    if role in user.roles:
      await ctx.send(f"{ctx.author.mention} nah bro I won't give u any")
    else:
      users = await get_bank_data()

      earnings = random.randrange(888, 2222)

      await ctx.send(
        f"{ctx.author.mention} earned **{earnings}** coins")

      users[str(user.id)]["Wallet"] += earnings

      with open("bank.json", 'w') as f:
        json.dump(users, f)
#work

  @commands.command()
  @commands.cooldown(1, 3600, commands.BucketType.user)
  @commands.guild_only()
  async def work(self, ctx):
    await open_account(ctx.author)

    user = ctx.author

    role = discord.utils.find(lambda r: r.name == 'jailed',
                              ctx.message.guild.roles)

    if role in user.roles:
      await ctx.send("ur jobless if u in jail lol".format(user))
    else:
      users = await get_bank_data()

      earnings = random.randrange(150)

      await ctx.send(f"{ctx.author.mention} earned **{earnings}** coins")

      users[str(user.id)]["Wallet"] += earnings

      with open("bank.json", 'w') as f:
        json.dump(users, f)
#rob other ppl money

  @commands.command()
  @commands.cooldown(1, 43200, commands.BucketType.user)
  @commands.guild_only()
  async def rob(self, ctx, member: discord.Member = None):
    user = ctx.author

    role = discord.utils.find(lambda r: r.name == 'jailed',
                              ctx.message.guild.roles)

    await open_account(ctx.author)
    await open_account(member)

    if role in user.roles:
      await ctx.send("man are u trying to double ur sentence or what")
    else:
      bal = await update_bank(member)

      if bal[0] < 100:
        await ctx.send("he's broke bro leave him alone")
        return

      earnings = random.randrange(0, bal[0])

      await update_bank(ctx.author, earnings)
      await update_bank(member, -1 * earnings)

      await ctx.send(
        f"{ctx.author.mention} stole {member.metion} **{earnings}** coins")
#give someone money

  @commands.command()
  @commands.guild_only()
  async def give(self, ctx, member: discord.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
      await ctx.send(f"{ctx.author.mention} tell me how much u wanna give ")
      return

    bal = await update_bank(ctx.author)
    amount = int(amount)

    if amount > bal[0]:
      await ctx.send("😂 no")
      return
    if amount < 0:
      await ctx.send("use rob instead")

    await update_bank(ctx.author, -1 * amount)
    await update_bank(member, amount, "Bank")

    await ctx.send(
      f"{ctx.author.mention} sent {member.mention} **{amount}** coins")

#slots machine

  @commands.command(pass_context=True, name="slot", aliases=["sl", "slots"])
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.guild_only()
  async def slots(self, ctx, amount: str = None):

    if amount == None:
      await ctx.send("bet ammount pls")
      return
    if amount.lower() in "all":
      await ctx.send(f"nope u can't do that")
    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[0]:
      await ctx.send("ok mr poverty, no")
      return
    if amount < 0:
      await ctx.send("are u trying to steal from casino or what")
      return
    if amount > 50000:
      await ctx.send("too much, the casino can't handle it")
      await ctx.send("max 50 000 coins")
      return
    slots = ['bus', 'train', 'horse', 'tiger', 'monkey', 'cow']
    slot1 = slots[random.randint(0, 5)]
    slot2 = slots[random.randint(0, 5)]
    slot3 = slots[random.randint(0, 5)]

    slotOutput = '| :{}: | :{}: | :{}: |\n'.format(slot1, slot2, slot3)

    ok = discord.Embed(title="Slots Machine", color=discord.Color(0xFFEC))
    ok.add_field(name="{}\nWon".format(slotOutput),
                 value=f'{ctx.author.mention} won **{2*amount}**coins')

    won = discord.Embed(title="Slots Machine", color=discord.Color(0xFFEC))
    won.add_field(
      name="{}\nWon".format(slotOutput),
      value=f'{ctx.author.mention} won **{3*amount}** coins, damn lucky bastard')

    lost = discord.Embed(title="Slots Machine", color=discord.Color(0xFFEC))
    lost.add_field(name="{}\nLost".format(slotOutput),
                   value=f'{ctx.author.mention} lost **{1*amount}** coins😂😂😂😂')

    if slot1 == slot2 == slot3:
      await update_bank(ctx.author, 3 * amount)
      await ctx.send(embed=won)
      return

    if slot1 == slot2:
      await update_bank(ctx.author, 2 * amount)
      await ctx.send(embed=ok)
      return

    if slot2 == slot3:
      await update_bank(ctx.author, 2 * amount)
      await ctx.send(embed=ok)
      return

    else:
      await update_bank(ctx.author, -1 * amount)
      await ctx.send(embed=lost)
      return

#roll dice

  @commands.command(name="rolldice",
                    aliases=["rd", "rdice", "dice", "roll_dice"])
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.guild_only()
  async def rolldice(self, ctx, amount=None):

    if amount == None:
      await ctx.send("wtf")
      return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[0]:
      await ctx.send("not enough ,get back to work")
      return
    if amount < 0:
      await ctx.send(f"{ctx.author.mention} idk. Maybe, just maybe use positive number u dumbass")
      return
    message = await ctx.send(
      "Chose 1 number:\n**4**, **6**, **8**, **10**, **12**, **20** ")

    def check(m):
      return m.author == ctx.author

    try:
      message = await self.bot.wait_for("message", check=check, timeout=30.0)
      m = message.content
      c = int(m)
      b = (random.randint(1, int(m)))
      if m != "4" and m != "6" and m != "8" and m != "10" and m != "12" and m != "20":
        await ctx.send("chose number from the list")
        return
      coming = await ctx.send("calling 🎲")
      time.sleep(3)
      await coming.delete()
      await ctx.send(f"dice stopped at: {b}")

      if b != c and b % 2 != 0:
        await update_bank(ctx.author, -1 * amount)
        await ctx.send(f"lost **{-1 * amount}** 😂")

        return
      if b == c:
        await update_bank(ctx.author, 3 * amount)
        await ctx.send(f"You won **{3*amount}** coins !")
        return
      if b == 1:
        await update_bank(ctx.author, -1 * amount)
        await ctx.send(f"You lost **{-1 * amount}** coins 😂😂😂😂😂😂😂😂😂 !")
        return
      if b != c and b % 2 == 0:
        await ctx.send(f"Tie")
        return

    except asyncio.TimeoutError:
      await message.delete()
      await ctx.send("damn bro answer me")



#coin flip

  @commands.command(name='coinflip', aliases=['coin_flip', 'cf'])
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.guild_only()
  async def coin_flip(self, ctx, amount=None, text=None):
    if amount == None:
      await ctx.send("how much?")
      return

    bal = await update_bank(ctx.author)
    amount = int(amount)

    if amount > bal[0]:
      await ctx.send(f"not enough ***{ctx.author}***")
      return
    if amount < 0:
      await ctx.send(f"has to be positive I guess ***{ctx.author}***")
      return

    if text is None:
      await ctx.send(f"***{ctx.author}*** chose head")
      time.sleep(1)
      coming = await ctx.send("Here it comes")
      time.sleep(3)
      await coming.delete()
      flip = random.randint(1, 2)
      if flip == 1:
        await update_bank(ctx.author, 2 * amount)
        await ctx.send(
          f"Coin stopped at head ***{ctx.author}*** won **{2 * amount}** coins"
        )
      else:
        await update_bank(ctx.author, -1 * amount)
        await ctx.send(
          f"Coins stopped at tail ***{ctx.author}*** lost **{-1 * amount}** coins lol"
        )

    if text in ['head', 'heads', 'Head', 'Heads']:
      await ctx.send(f"***{ctx.author}*** chose heads")
      time.sleep(1)
      coming = await ctx.send("Here it comes")
      time.sleep(3)
      await coming.delete()
      flip = random.randint(1, 2)
      if flip == 1:
        await update_bank(ctx.author, 2 * amount)
        await ctx.send(
          f"Coin stopped at head ***{ctx.author}*** won **{2 * amount}** coins"
        )
      else:
        await update_bank(ctx.author, -1 * amount)
        await ctx.send(
          f"Coins stopped at tail ***{ctx.author}*** lost **{-1 * amount}** coins lol"
        )

    if text in ['tail', 'tails', 'Tail', 'Tails']:
      await ctx.send(f"{ctx.author} chose Tail")
      time.sleep(1)
      coming = await ctx.send("Here it comes")
      time.sleep(3)
      await coming.delete()
      flip = random.randint(1, 2)
      if flip == 1:
        await update_bank(ctx.author, -1 * amount)
        await ctx.send(
          f"Coins stopped at head ***{ctx.author}*** lost **{-1 * amount}** coins lol"
        )
      else:
        await update_bank(ctx.author, 2 * amount)
        await ctx.send(
          f"Coins stopped at tail ***{ctx.author}*** won **{2 * amount}** coins*"
        )

  @work.error
  async def work_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(
        f'cí command coolingdown {round(error.retry_after/60, 2)}',
        delete_after=20)

  @beg.error
  async def beg_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(
        f'not yet usable ***{ctx.author}*** wait {round(error.retry_after/3600, 2)} more hours',
        delete_after=20)

  @daily.error
  async def daily_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(
        f'***{ctx.author}*** not yet man {round(error.retry_after/3600, 2)} more hours ',
        delete_after=20)

  @weekly.error
  async def weekly_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(
        f'{round(error.retry_after/86400, 2)} more days',
        delete_after=20)

  @rob.error
  async def rob_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(
        f'wait {round(error.retry_after/3600, 2)} more hours',
        delete_after=20)

  @slots.error
  async def slots_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(
        f'hang on {round(error.retry_after, 2)} for seconds',
        delete_after=20)

  @rolldice.error
  async def rolldice_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(
        f'hang on {round(error.retry_after, 2)} for senconds',
        delete_after=20)

  @coin_flip.error
  async def coin_flip_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send(
        f'***{ctx.author}*** hang on {round(error.retry_after, 2)} for seconds',
        delete_after=20)

  @jail.error
  async def jail_error(self, ctx, error):
    await ctx.send("impostor fr")

  @release.error
  async def release_error(self, ctx, error):
    await ctx.send("nope")
    await ctx.send(f"***{ctx.author}*** ur not in the gov")


async def setup(bot):
  await bot.add_cog(Economy(bot))
