import discord
from chiharu import *
from discord.ext import commands

class Initialize(ChiharuCog):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  @commands.Cog.listener()
  async def on_ready(self) -> None:
    print(f"Bot is ready! Logged in as {str(self.bot.user)} | ID: {self.bot.user.id}")


async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Initialize(bot))