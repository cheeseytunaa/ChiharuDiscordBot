import discord
from chiharu import *
from discord.ext import commands

class DebugCommand(ChiharuCog):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  @commands.command()
  async def debug(self, ctx: commands.Context, mode: str = None):
    config = get_json_data("data/config.json")
    config["debug_mode"] = not config["debug_mode"] if not mode else True if mode.lower() == "true" else False
    save_json_data("data/config.json", config)
    await ctx.send(f"Debug mode: **{config['debug_mode']}**")

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(DebugCommand(bot))