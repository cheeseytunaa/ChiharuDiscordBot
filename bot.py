from chiharu import *
import discord
from discord.ext import commands

import sys
sys.dont_write_bytecode = True

config = get_json_data("data/config.json")
PREFIX = config["prefix"]
VERSION = config["version"]
WEBSITE_DOMAIN = config["website_domain"]

class ChiharuChan(commands.Bot):
  def __init__(self) -> None:
    intents = discord.Intents.default()
    intents.message_content = True
    super().__init__(command_prefix=PREFIX, intents=intents)
    self.remove_command("help")

  async def setup_hook(self) -> None:
    cog_folders = [folder for folder in get_sub_directories(".") if folder.startswith("_") and folder != "__pycache__"]
    for folder in cog_folders:
      for extension in get_files(folder):
        await self.load_extension(f"{folder}.{extension[:-3]}")

bot = ChiharuChan()
bot.current_language = get_json_data("data/config.json")["language"].lower()
bot.language_data = get_language_data(bot.current_language)

bot.run(get_token())