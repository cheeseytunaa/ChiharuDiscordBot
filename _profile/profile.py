import discord
from chiharu import *
from discord.ext import commands

from _profile import create

class Profile(ChiharuCog):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  @commands.command(aliases=get_alias_data("profile"))
  async def profile(self, ctx, user: discord.Member = None) -> None:
    command_language_data = self.bot.language_data["command_display_profile"]
    author = ctx.author
    user = user or ctx.author

    stable_property_list = create.CreateProfile(self.bot).stable_property_list
    special_property_list = create.CreateProfile(self.bot).special_property_list

    if f"{str(user.id)}.json" in get_files("data/profiles"):
      user_data = get_json_data(f"data/profiles/{str(user.id)}.json")
      for key in list(user_data.keys()):
        if not user_data[key] and key not in stable_property_list + special_property_list:
          user_data[key] = self.bot.language_data["variables"]["no_information"]
        if isinstance(user_data[key], list) and key not in stable_property_list + special_property_list:
          user_data[key] = ", ".join(user_data[key])
        if not user_data[key] and key == "description":
          user_data[key] = self.bot.language_data["variables"]["no_description"]

      for key in list(user_data["intimacy"].keys()):
        if not user_data["intimacy"][key]:
          user_data["intimacy"][key] = self.bot.language_data["variables"]["no_information"]
        if isinstance(user_data["intimacy"][key], list):
          user_data["intimacy"][key] = ", ".join(user_data["intimacy"][key])

      if user_data["date_of_birth"]:
        day, month, year = user_data["date_of_birth"]
        user_data["date_of_birth"] = f"{str(day).zfill(2)}/{str(month).zfill(2)}/{str(year).zfill(2)}"
        current_day, current_month, current_year = date()
        if current_month < month:
          age = current_year - year - 1
        elif current_month == month and current_day < day:
          age = current_year - year - 1
        else:
          age = current_year - year
      else:
        user_data["date_of_birth"] = age = self.bot.language_data["variables"]["no_information"]

      gender_switcher = {
        0: "no_information",
        1: "male",
        2: "female",
        3: "LGBT",
        4: "hidden"
      }
      if user_data["gender"] in gender_switcher and user_data["gender"] != 0:
        user_data["gender"] = self.bot.language_data["variables"]["genders"][gender_switcher[user_data["gender"]]]
      else:
        user_data["gender"] = self.bot.language_data["variables"][gender_switcher[0]]

      profile_message_data = HData(command_language_data["profile_to_be_displayed"])
      display_content = profile_message_data[2].copy()
      for line_index in range(len(display_content)):
        if [hidden_key for hidden_key in user_data["hidden"] if hidden_key.upper() in display_content[line_index]]:
          display_content[line_index] = None
        else:
          display_content[line_index] = display_content[line_index].format(
            DESCRIPTION=user_data["description"],
            IRL_NAME=user_data["irl_name"],
            FRIENDLY_NAME=user_data["friendly_name"],
            ADDRESS=user_data["address"],
            PHONE_NUMBER=user_data["phone_number"],
            NATIONALITY=user_data["nationality"],
            DATE_OF_BIRTH=user_data["date_of_birth"],
            AGE=age,
            GENDER=user_data["gender"],
            IG_NAME=user_data["ig_name"],
            DISCORD=user_data["discord"],
            SCHOOL=user_data["school"],
            CLASS=user_data["class"],
            GAMES=user_data["games"],
            GIRL_FRIEND=user_data["intimacy"]["girl_friend"],
            BOY_FRIEND=user_data["intimacy"]["boy_friend"],
            BEST_FRIENDS=user_data["intimacy"]["best_friends"],
            FRIENDS=user_data["intimacy"]["friends"]
          )
      profile_message_data[2] = [line for line in display_content if line is not None]  # Remove None lines without removing empty strings (which represent new lines)
      profile_message_data.replace_var("{USERNAME}", str(user))
      profile_message_embed = HEmbed(profile_message_data)
      profile_message_embed.color = get_color(user_data["color"])
      profile_message_embed.url = user_data["link"] if user_data["link"] else "https://youtu.be/dQw4w9WgXcQ"
      profile_message_embed.set_thumbnail(url=user.avatar.url)
      profile_message_embed.set_author(name=command_language_data["author_title_display"].replace("{EXECUTOR}", str(author)), icon_url=author.avatar.url)
      profile_message_embed.set_image(url=user_data["image"] if user_data["image"] else "")
      await ctx.reply(embed=profile_message_embed, mention_author=False)
    else:
      no_profile_message_data = HData(command_language_data["profile_not_found"])
      no_profile_message_data.replace_var("{USERNAME}", str(user))
      await ctx.reply(embed=HEmbed(no_profile_message_data), mention_author=False)

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Profile(bot))