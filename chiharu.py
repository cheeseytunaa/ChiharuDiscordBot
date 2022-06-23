"""
This is where the utility functions for the Chiharu are defined.
Read the 'readme.md' file for more information about how to use these functions and classes!
"""

from multimethod import multimethod
from discord.ext import commands
import discord
import json
import datetime
import dotenv
import os


# Color constants
COLORS = {
  "CHAOCHAODEPTRAI": "#ffc0cb",
  "RED": "#ff0000",
  "GREEN": "#00ff00",
  "BLUE": "#0000ff",
  "YELLOW": "#ffff00",
  "PINK": "#ff00ff",
  "PURPLE": "#8A2BE2",
  "CYAN": "#00ffff",
  "WHITE": "#ffffff",
  "BLACK": "#000000",
  "ORANGE": "#ffa500",
  "BROWN": "#a52a2a",
  "GREY": "#808080",
  "DARK_GREY": "#404040",
  "LIGHT_GREY": "#c0c0c0",
  "DARK_GREEN": "#006400",
  "LIGHT_GREEN": "#90ee90",
  "DARK_BLUE": "#00008b",
  "LIGHT_BLUE": "#add8e6",
  "DARK_PURPLE": "#800080",
  "LIGHT_PURPLE": "#e6e6fa",
  "DARK_CYAN": "#008b8b",
  "LIGHT_CYAN": "#00ffff",
  "DARK_RED": "#8b0000",
  "LIGHT_RED": "#ffb6c1",
  "DARK_ORANGE": "#ff8c00",
  "LIGHT_ORANGE": "#ffa07a",
  "DARK_BROWN": "#a52a2a",
  "LIGHT_BROWN": "#deb887",
  "DARK_GOLD": "#ffd700",
  "LIGHT_GOLD": "#ffefd5",
  "DARK_SILVER": "#c0c0c0",
  "LIGHT_SILVER": "#e0e0e0",
  "DARK_PINK": "#ff1493",
  "LIGHT_PINK": "#ffb6c1",
  # Down here are legacy ones (Used for backwards compatibility / Usually not used because of their deprecations)
  "C_RED": 0xff0000,
  "C_GREEN": 0x00ff00,
  "C_BLUE": 0x0000ff,
  "C_YELLOW": 0xffff00,
  "C_PURPLE": 0xff00ff, 
  "C_CYAN": 0x00ffff,
  "C_WHITE": 0xffffff,
  "C_BLACK": 0x000000
}


class ChiharuCog(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    super().__init__()
    self.bot = bot


# Get TOKEN value from .env file
def get_token() -> str:
  dotenv.load_dotenv()
  return os.getenv("TOKEN")


# JSON handler
def get_json_data(directory: str) -> dict or list or tuple or set:
  with open(directory, "r", encoding="utf-8") as file:
    return json.load(file)


def save_json_data(directory: str, data: dict) -> None:
  with open(directory, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)


def get_language_data(current_language: str) -> dict:
  return get_json_data(f"data/languages/{current_language}.json")


def get_alias_data(command: str = None) -> dict:
  data = get_json_data(f"data/command_alias.json")
  if not command or command not in list(data.keys()):
    return data
  else:
    return data[command]


# Color codes handler
def get_color(color: str, type_to_convert_to="hex") -> int:
  type_to_convert_to = type_to_convert_to.lower()
  if color in COLORS:
    color = COLORS[color]
    color = color.strip("#")
    return int(color, 16)

  color = color.strip("#")
  if type_to_convert_to in ["hex", 16]:
    return int(color, 16)
  elif type_to_convert_to in ["dec", 10]:
    return int(color)
  else:
    return int("ff0000", 16)


# Get time and date
def time() -> tuple:
  current_time = datetime.datetime.utcnow()
  return current_time.hour, current_time.minute, current_time.second


def date() -> tuple:
  current_date = datetime.datetime.utcnow()
  return current_date.day, current_date.month, current_date.year


# Get all files in a directory
def get_files(directory: str) -> list:
  # return os.listdir(directory) # This is the old way / deprecated
  return [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]


# Get all sub-directories in a directory
def get_sub_directories(directory: str) -> list:
  return [sub_directory for sub_directory in os.listdir(directory) if os.path.isdir(os.path.join(directory, sub_directory))]


# Remove file
def delete_file(directory: str) -> None:
  os.remove(directory)


# Get flag emoji
def get_flag_emoji(country: str) -> str:
  # return discord.utils.get(bot.get_all_emojis(), name=country) # This is the old way / deprecated
  flag_emoji = ""
  flag_code = get_json_data("data/flag_code.json")
  for letter_index in range(len(country)):
    flag_emoji += get_json_data("data/unicode_regional_indicator.json")[country[letter_index]]
  return flag_emoji if flag_emoji in flag_code.values() else "💔"


# Embed builder class
class HEmbed(discord.Embed):
  """
  This class is used to create embeds for the bot.
  """
  @multimethod
  def __init__(self, content: list):
    super().__init__(title=content[0])
    self.color = get_color(content[1])
    if isinstance(content[2], str):
      self.description = content[2]
    elif isinstance(content[2], list):
      self.description = "\n".join(content[2])
    self.set_footer(
      text="Coded by _NooberrUwU#3652 | v{}".format(get_json_data("data/config.json")["version"]),
      icon_url="https://cdn.discordapp.com/attachments/947780453744672798/976852966063624242/koolcat.jpg"
    )

  @multimethod
  def __init__(self, title: str, color: str, description):
    super().__init__(title=title)
    self.color = get_color(color)
    if isinstance(description, str):
      self.description = description
    elif isinstance(description, list):
      self.description = "\n".join(description)
    self.set_footer(
      text="Coded by _NooberrUwU#3652 | v{}".format(get_json_data("data/config.json")["version"]),
      icon_url="https://cdn.discordapp.com/attachments/947780453744672798/976852966063624242/koolcat.jpg"
    )


# Embed data builder class
class HData(list):
  """
  This class is used to handle embed data.
  """
  def __init__(self, content: list):
    super().__init__(content)

  def replace_var(self, var: str, value: str):
    def replacement(original, string_1, string_2):
      if isinstance(original, str):
        return original.replace(string_1, string_2)
      elif isinstance(original, list):
        return [replacement(i, string_1, string_2) for i in original]
      else:
        return original

    for item_index in range(len(self)):
      self[item_index] = replacement(self[item_index], var, value)


# Ended prompt view
class EndedView(discord.ui.View):
  language_data = get_language_data(get_json_data("data/config.json")["language"])

  @discord.ui.button(
    label=language_data["variables"]["ended_prompt_button_label"],
    disabled=True,
    style=discord.ButtonStyle.gray,
    emoji="⏹️"
  )
  async def ended_prompt(self, interaction, button):
    pass


# Not author data builder class
def not_author(user: discord.User) -> HData:
  language_data = get_language_data(get_json_data("data/config.json")["language"])
  not_author_message_data = HData(language_data["variables"]["not_author"])
  not_author_message_data.replace_var("{USERNAME}", str(user))
  return not_author_message_data
