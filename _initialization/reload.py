import discord
from chiharu import *
from discord.ext import commands

class Reload(ChiharuCog):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  @commands.command()
  async def reload(self, ctx: commands.Context, folder: str = "all") -> None:
    # await ctx.send(f"Reloading folder: **{folder}**")
    cog_list = []
    if folder != "all" and folder in get_sub_directories("."):
      for extension in get_files(f"{folder}"):
        try:
          await self.bot.unload_extension(f"{folder}.{extension[:-3]}")
        except commands.ExtensionNotLoaded:
          await ctx.send(f"{folder}.{extension[:-3]} cannot be unloaded! Don't worry, it will be reloaded!")
        # await ctx.send(f"Unloaded successfully: **{folder}.{extension[:-3]}**")
        cog_list.append(f"{folder}.{extension[:-3]}")
      for cog in cog_list:
        await self.bot.load_extension(cog)
        # await ctx.send(f"Loaded successfully: **{cog}**")
    else:
      for folder in [folder for folder in get_sub_directories(".") if folder.startswith("_") and folder != "__pycache__"]:
        for extension in get_files(f"{folder}"):
          try:
            await self.bot.unload_extension(f"{folder}.{extension[:-3]}")
          except commands.ExtensionNotLoaded:
            await ctx.send(f"{folder}.{extension[:-3]} cannot be unloaded! Don't worry, it will be reloaded!")
          # await ctx.send(f"Unloaded successfully: **{folder}.{extension[:-3]}**")
          cog_list.append(f"{folder}.{extension[:-3]}")
      for cog in cog_list:
        await self.bot.load_extension(cog)
        # await ctx.send(f"Loaded successfully: **{cog}**")

    await ctx.send("Reloaded!")

  @commands.Cog.listener()
  async def on_message(self, message):
    if all([
      get_json_data("data/config.json")["debug_mode"],
      not message.author.bot,
    ]):
      if message.author.guild_permissions.administrator and message.content in ["bot rl", "bot reload", "reload", "rl", "sos", "et o et", "etoet"]:
        await self.reload(commands.Context(message=message, bot=self.bot, view=None))

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Reload(bot))