from tkinter import NONE
from chiharu import *
from discord.ext import commands

class CreateProfile(ChiharuCog):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  @commands.command(aliases=get_alias_data()["create"])
  async def create(self, ctx):
    user_profile_template = {
      "color": COLORS["CYAN"],
      "link": "",
      "image": "",
      "discord": str(ctx.author),
      "irl_name": "",
      "friendly_name": "",
      "address": "",
      "phone_number": None,
      "nationality": "",
      "date_of_birth": [],
      "gender": 0,
      "ig_name": "",
      "games": [],
      "description": "",
      "school": "",
      "class": "",
      "intimacy": {
        "girl_friend": "",
        "boy_friend": "",
        "best_friends": [],
        "friends": []
      },
      "hidden": []
    }
    command_language_data = self.bot.language_data["command_create_profile"]
    author_id = ctx.author.id
    if f"{str(author_id)}.json" not in get_files("data/profiles"):
      save_json_data(f"data/profiles/{str(author_id)}.json", user_profile_template)
      success_message_data = HData(command_language_data["created_successfully"])
      success_message_data.replace_var("{PREFIX}", ctx.prefix)
      await ctx.reply(embed=HEmbed(success_message_data), mention_author=False)
    else:
      error_message_data = HData(command_language_data["profile_already_existed"])
      error_message_data.replace_var("{PREFIX}", await self.bot.get_prefix(ctx))
      await ctx.reply(embed=HEmbed(error_message_data), mention_author=False)


async def setup(bot) -> None:
  await bot.add_cog(CreateProfile(bot))