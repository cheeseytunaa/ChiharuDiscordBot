import discord
from chiharu import *
from discord.ext import commands

import os

class ClearTerminal(ChiharuCog):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  @commands.command()
  async def clearterminal(self, ctx: commands.Context) -> None:
    os.system("CLS")
    await ctx.send("The terminal has been cleared!")

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(ClearTerminal(bot))