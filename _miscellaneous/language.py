import discord
from chiharu import *
from discord.ext import commands

class Language(ChiharuCog):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  @commands.command(aliases=get_alias_data("language"))
  async def language(self, ctx: commands.Context, language: str = None) -> None:
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
        command_language_data = self.bot.language_data["command_language"]
        language_not_found_message_data = HData(command_language_data["language_not_found"])
        language_not_found_message_data.replace_var("{PREFIX}", ctx.prefix)
        await ctx.reply(embed=HEmbed(language_not_found_message_data), mention_author=False)
    else:
      command_language_data = self.bot.language_data["command_language"]
      
      class LanguageOptions(discord.ui.View):
        @discord.ui.button(label=command_language_data["change_language_button_label"], style=discord.ButtonStyle.green)
        async def change_language_button(self, interaction, button):
          if interaction.user != ctx.author:
            return await interaction.response.send_message(embed=HEmbed(not_author(interaction.user)), ephemeral=True)
          change_language_message_data = HData(command_language_data["change_language_guide"])
          change_language_message_data.replace_var("{PREFIX}", ctx.prefix)
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

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Language(bot))