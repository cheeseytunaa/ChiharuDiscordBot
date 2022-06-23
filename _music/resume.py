import discord
from chiharu import *
from discord.ext import commands

class Resume(ChiharuCog):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  @commands.command()
  async def resume(self, ctx: commands.Context) -> None:
    ctx.voice_client.resume()

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Resume(bot))