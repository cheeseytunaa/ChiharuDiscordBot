import discord
from chiharu import *
from discord.ext import commands

from _profile import create

class ConfigProfile(ChiharuCog):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  @commands.command(aliases=get_alias_data("config"))
  async def config(self, ctx: commands.Context, key: str = None, *value: str):
    command_language_data = self.bot.language_data["command_config_profile"]
    author = ctx.author

    class ChooseAction(discord.ui.View):
      @discord.ui.button(label=command_language_data["config_button_label"], style=discord.ButtonStyle.green)
      async def config_button(self, interaction, button):
        if interaction.user != ctx.author:
          return await interaction.response.send_message(embed=HEmbed(not_author(interaction.user)), ephemeral=True)
        config_guide_message_data = HData(command_language_data["config_guide"])
        config_guide_message_data.replace_var("{PREFIX}", ctx.prefix)
        config_guide_message_data.replace_var("{TUTORIAL_BUTTON_LABEL}", command_language_data["tutorial_button_label"])
        await interaction.response.send_message(embed=HEmbed(config_guide_message_data), ephemeral=True, view=ConfigProfile())
        await choose_action_message.edit(view=EndedView())

      @discord.ui.button(label=command_language_data["tutorial_button_label"], style=discord.ButtonStyle.gray)
      async def tutorial_button(self, interaction, button):
        pass

    class ConfigProfile(discord.ui.View):
      user_template = create.CreateProfile(self.bot).user_profile_template
      config_options = []
      available_keys = list(user_template.keys())
      available_keys = [key for key in available_keys if key not in create.CreateProfile(self.bot).uneditable_property_list]
      parent_keys = create.CreateProfile(self.bot).parent_property_list
      children_keys = []
      for parent_key in parent_keys:
        children_keys += user_template[parent_key]
      for property_name in available_keys + children_keys:
        config_options.append(discord.SelectOption(label=property_name))
      
      @discord.ui.select(options=config_options, min_values=0, max_values=5)
      async def choose_property(self, interaction, select):
        await interaction.response.send_modal(ConfigModal(select.values))

    class ConfigModal(discord.ui.Modal, title="Configure Profile"):
      def __init__(self, properties: list):
        super().__init__()
        self.properties = properties
        for property in properties:
          self.add_item(discord.ui.TextInput(label=f"{property}"))
      async def on_submit(self, interaction):
        await interaction.response.send_message(f"{self.children[0].value}", ephemeral=True)
        user_data = get_json_data(f"data/profiles/{str(author.id)}.json")
        for property_index in range(len(self.properties)):
          user_data[self.properties[property_index]] = self.children[property_index].value
        save_json_data(f"data/profiles/{str(author.id)}.json", user_data)

    if f"{str(author.id)}.json" in get_files("data/profiles"):
      choose_action_message_data = HData(command_language_data["choose_action"])
      choose_action_message_data.replace_var("{PREFIX}", ctx.prefix)
      choose_action_message_data.replace_var("{CONFIG_BUTTON_LABEL}", command_language_data["config_button_label"])
      choose_action_message_data.replace_var("{TUTORIAL_BUTTON_LABEL}", command_language_data["tutorial_button_label"])
      choose_action_message = await ctx.reply(embed=HEmbed(choose_action_message_data), view=ChooseAction(), mention_author=False)
    else:
      error_message_data = HData(self.bot.language_data["command_display_profile"]["profile_not_found"])
      error_message_data.replace_var("{USERNAME}", str(author))
      await ctx.reply(embed=HEmbed(error_message_data), mention_author=False)

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(ConfigProfile(bot))