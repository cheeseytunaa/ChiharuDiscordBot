import discord
from chiharu import *
from discord.ext import commands

class Leave(ChiharuCog):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  @commands.command()
  async def leave(self, ctx: commands.Context) -> None:
    if ctx.voice_client is None:
      await ctx.send("I'm not currently in any voice channel!")
    elif ctx.voice_client.channel == ctx.author.voice.channel:
      await ctx.send(f"Left **{ctx.voice_client.channel}**.")
      await ctx.voice_client.disconnect()
    else:
      await ctx.send("We are not currently in the same voice channel!")

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Leave(bot))