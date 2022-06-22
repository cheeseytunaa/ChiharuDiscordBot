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
    await self.load_extension("_initialization.init")
    await self.load_extension("_profile.create")

bot = ChiharuChan()
bot.current_language = current_language = get_json_data("data/config.json")["language"].lower()
bot.aliases_data = aliases_data = get_json_data("data/command_alias.json")
bot.language_data = language_data = get_language_data(current_language)


@bot.command(aliases=aliases_data["language"])
async def language(ctx, language: str = None):
  current_language = get_json_data("./data/config.json")["language"]
  available_languages = [name.replace(".json", "") for name in get_files("data/languages")]
  
  def change_language(language_to_change_to: str):
    global language_data
    current_language = language_to_change_to.lower()
    language_data = get_language_data(current_language)
    config_data = get_json_data("data/config.json")
    config_data["language"] = language_to_change_to.lower()
    save_json_data("data/config.json", config_data)
    return_text = HData(get_language_data(language_to_change_to)["command_language"]["changed_successfully"])
    return_text.replace_var("{NEW_LANGUAGE}", language_to_change_to)
    return return_text
  
  if language:
    if language.lower() in available_languages:
      await ctx.reply(embed=HEmbed(change_language(language)), mention_author=False)
    else:
      command_language_data = language_data["command_language"]
      language_not_found_message_data = HData(command_language_data["language_not_found"])
      language_not_found_message_data.replace_var("{PREFIX}", PREFIX)
      await ctx.reply(embed=HEmbed(language_not_found_message_data), mention_author=False)
  else:
    command_language_data = language_data["command_language"]
    
    class LanguageOptions(discord.ui.View):
      @discord.ui.button(label=command_language_data["change_language_button_label"], style=discord.ButtonStyle.green)
      async def change_language_button(self, interaction, button):
        if interaction.user != ctx.author:
          return await interaction.response.send_message(embed=HEmbed(not_author(interaction.user)), ephemeral=True)
        change_language_message_data = HData(command_language_data["change_language_guide"])
        change_language_message_data.replace_var("{PREFIX}", PREFIX)
        await interaction.response.send_message(embed=HEmbed(change_language_message_data), view=ChooseLanguage(), ephemeral=True)
        await info_message.edit(view=EndedView())

      @discord.ui.button(label=command_language_data["localization_button_label"], style=discord.ButtonStyle.gray)
      async def localization_button(self, interaction, button):
        if interaction.user != ctx.author:
          not_author_message_data = HData(language_data["variables"]["not_author"])
          not_author_message_data.replace_var("{USERNAME}", str(interaction.user))
          return await interaction.response.send_message(embed=HEmbed(not_author_message_data), ephemeral=True)
        await info_message.edit(view=EndedView())

    class ChooseLanguage(discord.ui.View):
      language_options = []
      for language in available_languages:
        language_configurations = get_json_data(f"data/languages/{language}.json")["language_configurations"]
        language_options.append(
          discord.SelectOption(
            label=language_configurations["language"] + " | " + language_configurations["language_code"],
            value=language_configurations["language_file"],
            description=language_configurations["language_name"],
            emoji=get_flag_emoji(language_configurations["flag_code"]),
            default=True if language_configurations["language_file"] == current_language else False
          )
        )
      @discord.ui.select(options=language_options, placeholder=get_json_data(f"data/languages/{language}.json")["command_language"]["choose_language_placeholder"])
      async def choose_language(self, interaction, select):
        await interaction.response.edit_message(embed=HEmbed(change_language(select.values[0])), view=None)

    info_message_data = HData(command_language_data["info"])
    info_message_data.replace_var("{NUMBER}", str(len(available_languages)))
    info_message_data.replace_var("{LANGUAGES}", ", ".join(available_languages))
    info_message_data.replace_var("{CURRENT_LANGUAGE}", current_language)
    info_message = await ctx.reply(embed=HEmbed(info_message_data), view=LanguageOptions(), mention_author=False)

user_profile_template = {
  "color": COLORS["CYAN"],
  "link": "",
  "image": "",
  "discord": "",
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
stable_property_list = ["intimacy", "hidden", "color", "link", "image"]  # These properties are not shown as parts of the profile (at least in a proper way)
special_property_list = ["date_of_birth", "gender", "description"]  # These properties need handling
# @bot.command(aliases=aliases_data["create"])
# async def create(ctx):
#   command_language_data = language_data["command_create_profile"]
#   author_id = ctx.author.id
#   if f"{str(author_id)}.json" not in get_files("data/profiles"):
#     user_profile = user_profile_template.copy()
#     user_profile["discord"] = str(ctx.author)
#     save_data(f"data/profiles/{str(author_id)}.json", user_profile)
#     success_message_data = HData(command_language_data["created_successfully"])
#     success_message_data.replace_var("{PREFIX}", PREFIX)
#     await ctx.reply(embed=HEmbed(success_message_data), mention_author=False)
#   else:
#     error_message_data = HData(command_language_data["profile_already_existed"])
#     error_message_data.replace_var("{PREFIX}", PREFIX)
#     await ctx.reply(embed=HEmbed(error_message_data), mention_author=False)


@bot.command(aliases=aliases_data["delete"])
async def delete(ctx):
  command_language_data = language_data["command_delete_profile"]
  author_id = ctx.author.id

  class ConfirmView(discord.ui.View):
    @discord.ui.button(label=command_language_data["button_yes_label"], style=discord.ButtonStyle.green)
    async def yes(self, interaction, button):
      if interaction.user != ctx.author:
        return await interaction.response.send_message(embed=HEmbed(not_author(interaction.user)), ephemeral=True)
      await interaction.response.send_message(embed=HEmbed(command_language_data["deleted_successfully"]), ephemeral=True, view=None)
      await confirm_message.edit(view=EndedView())
      delete_file(f"data/profiles/{str(author_id)}.json")
    
    @discord.ui.button(label=command_language_data["button_no_label"], style=discord.ButtonStyle.red)
    async def no(self, interaction, button):
      if interaction.user != ctx.author:
        return await interaction.response.send_message(embed=HEmbed(not_author(interaction.user)), ephemeral=True)
      await interaction.response.send_message(embed=HEmbed(command_language_data["undid_successfully"]), ephemeral=True, view=None)
      await confirm_message.edit(view=EndedView())

  if f"{str(author_id)}.json" in get_files("data/profiles"):
    confirm_message = await ctx.reply(embed=HEmbed(command_language_data["confirm_delete"]), view=ConfirmView(), mention_author=False)
  else:
    await ctx.reply(embed=HEmbed(command_language_data["profile_not_found"]), mention_author=False)


@bot.command(aliases=aliases_data["profile"])
async def profile(ctx, user: discord.Member = None):
  command_language_data = language_data["command_display_profile"]
  author = ctx.author
  user = user or ctx.author
  if f"{str(user.id)}.json" in get_files("data/profiles"):
    user_data = get_json_data(f"data/profiles/{str(user.id)}.json")
    for key in list(user_data.keys()):
      if not user_data[key] and key not in stable_property_list + special_property_list:
        user_data[key] = language_data["variables"]["no_information"]
      if isinstance(user_data[key], list) and key not in stable_property_list + special_property_list:
        user_data[key] = ", ".join(user_data[key])
      if not user_data[key] and key == "description":
        user_data[key] = language_data["variables"]["no_description"]

    for key in list(user_data["intimacy"].keys()):
      if not user_data["intimacy"][key]:
        user_data["intimacy"][key] = language_data["variables"]["no_information"]
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
      user_data["date_of_birth"] = age = language_data["variables"]["no_information"]

    gender_switcher = {
      0: "no_information",
      1: "male",
      2: "female",
      3: "LGBT",
      4: "hidden"
    }
    if user_data["gender"] in gender_switcher and user_data["gender"] != 0:
      user_data["gender"] = language_data["variables"]["genders"][gender_switcher[user_data["gender"]]]
    else:
      user_data["gender"] = language_data["variables"][gender_switcher[0]]

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


@bot.command(aliases=aliases_data["config"])
async def config(ctx, key: str = None, *value: str):
  command_language_data = language_data["command_config_profile"]
  author = ctx.author

  class ChooseAction(discord.ui.View):
    @discord.ui.button(label=command_language_data["config_button_label"], style=discord.ButtonStyle.green)
    async def config_button(self, interaction, button):
      if interaction.user != ctx.author:
        return await interaction.response.send_message(embed=HEmbed(not_author(interaction.user)), ephemeral=True)
      config_guide_message_data = HData(command_language_data["config_guide"])
      config_guide_message_data.replace_var("{PREFIX}", PREFIX)
      config_guide_message_data.replace_var("{TUTORIAL_BUTTON_LABEL}", command_language_data["tutorial_button_label"])
      await interaction.response.send_message(embed=HEmbed(config_guide_message_data), ephemeral=True, view=ConfigProfile())
      await choose_action_message.edit(view=EndedView())

    @discord.ui.button(label=command_language_data["tutorial_button_label"], style=discord.ButtonStyle.gray)
    async def tutorial_button(self, interaction, button):
      pass
    
  class ConfigProfile(discord.ui.View):
    config_options = []
    for property_name in ['color', 'link', 'image', 'discord', 'irl_name', 'friendly_name', 'address', 'phone_number', 'nationality', 'date_of_birth', 'gender', 'ig_name', 'games', 'description', 'school', 'class', 'girl_friend', "boy_friend", "friends", "best_friends", 'hidden']:
      config_options.append(discord.SelectOption(label=property_name))
    @discord.ui.select(options=config_options, min_values=0, max_values=5)
    async def choose_property(self, interaction, select):
      await interaction.response.send_modal(ConfigModal(select.values))

  class ConfigModal(discord.ui.Modal, title="Configure Profile"):
    def __init__(self, properties : list):
      super().__init__()
      for property in properties:
        self.add_item(discord.ui.TextInput(label=f"{property}"))
    async def on_submit(self, interaction):
      await interaction.response.send_message(f"{self.children[0].value}", ephemeral=True)

  if f"{str(author.id)}.json" in get_files("data/profiles"):
    user_data = get_json_data(f"data/profiles/{str(author.id)}.json") 

    choose_action_message_data = HData(command_language_data["choose_action"])
    choose_action_message_data.replace_var("{PREFIX}", PREFIX)
    choose_action_message_data.replace_var("{CONFIG_BUTTON_LABEL}", command_language_data["config_button_label"])
    choose_action_message_data.replace_var("{TUTORIAL_BUTTON_LABEL}", command_language_data["tutorial_button_label"])
    choose_action_message = await ctx.reply(embed=HEmbed(choose_action_message_data), view=ChooseAction(), mention_author=False)
  else:
    error_message_data = HData(language_data["command_display_profile"]["profile_not_found"])
    error_message_data.replace_var("{USERNAME}", str(author))
    await ctx.reply(embed=HEmbed(error_message_data), mention_author=False)


@bot.command()
async def feedback(ctx):
  command_language_data = language_data["command_feedback"]

  class Feedback(discord.ui.Modal, title=command_language_data["popup_window"]["title"]):
    feedback = discord.ui.TextInput(
      label="Feedback:",
      style=discord.TextStyle.paragraph,
      placeholder=command_language_data["popup_window"]["feedback_input_placeholder"]
    )
    anonymously_sent = discord.ui.TextInput(
      label="Send in incognito-mode: ",
      placeholder=command_language_data["popup_window"]["incognito_send_input_placeholder"],
      max_length=10,
      required=False
    )

    async def on_submit(self, interaction: discord.Interaction):
      await interaction.response.send_message(embed=HEmbed(command_language_data["feedback_sent"]), ephemeral=True)
      feedback_data = get_json_data("data/feedback.json")
      if self.anonymously_sent.value.lower() in ["yes", "true"]:
        self.anonymously_sent = True
      else:
        self.anonymously_sent = False
      user_feedback = {
        "recommender_id": interaction.user.id,
        "anonymously_sent": self.anonymously_sent,
        "content": self.feedback.value
      }
      feedback_data.append(user_feedback)
      save_json_data("data/feedback.json", feedback_data)

  class FeedbackView(discord.ui.View):
    @discord.ui.button(label=command_language_data["button_feedback_label"], style=discord.ButtonStyle.gray, emoji="📨")
    async def feedback(self, interaction, button):
      if interaction.user != ctx.author:
        return await interaction.response.send_message(embed=HEmbed(not_author(interaction.user)), ephemeral=True)
      await guide_message.edit(view=EndedView())
      await interaction.response.send_modal(Feedback())

  guide_message = await ctx.send(embed=HEmbed(command_language_data["feedback_guide"]), view=FeedbackView())


bot.run(get_token())