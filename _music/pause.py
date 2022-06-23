import discord
from chiharu import *
from discord.ext import commands

class Pause(ChiharuCog):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  @commands.command()
  async def pause(self, ctx: commands.Context) -> None:
    ctx.voice_client.pause()

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Pause(bot))