from chiharu import *
from discord.ext import commands

class Initialize(commands.Cog):
  def __init__(self, bot) -> None:
    super().__init__()
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self) -> None:
    print(f"Bot is ready! Logged in as {str(self.bot.user)} | ID: {self.bot.user.id}")


async def setup(bot) -> None:
  await bot.add_cog(Initialize(bot))