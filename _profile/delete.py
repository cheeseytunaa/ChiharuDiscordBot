import discord
from chiharu import *
from discord.ext import commands

class DeleteProfile(ChiharuCog):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  @commands.command(aliases=get_alias_data("delete"))
  async def delete(self, ctx: commands.Context) -> None:
    command_language_data = self.bot.language_data["command_delete_profile"]
    author_id = ctx.author.id

    class ConfirmView(discord.ui.View):
      @discord.ui.button(label=command_language_data["button_yes_label"], style=discord.ButtonStyle.green)
      async def yes(self, interaction, button):
        if interaction.user != ctx.author:
          return await interaction.response.send_message(embed=HEmbed(not_author(interaction.user)), ephemeral=True)
        await interaction.response.send_message(embed=HEmbed(command_language_data["deleted_successfully"]), ephemeral=True)
        await confirm_message.edit(view=EndedView())
        delete_file(f"data/profiles/{str(author_id)}.json")
      
      @discord.ui.button(label=command_language_data["button_no_label"], style=discord.ButtonStyle.red)
      async def no(self, interaction, button):
        if interaction.user != ctx.author:
          return await interaction.response.send_message(embed=HEmbed(not_author(interaction.user)), ephemeral=True)
        await interaction.response.send_message(embed=HEmbed(command_language_data["undid_successfully"]), ephemeral=True)
        await confirm_message.edit(view=EndedView())

    if f"{str(author_id)}.json" in get_files("data/profiles"):
      confirm_message = await ctx.reply(embed=HEmbed(command_language_data["confirm_delete"]), view=ConfirmView(), mention_author=False)
    else:
      await ctx.reply(embed=HEmbed(command_language_data["profile_not_found"]), mention_author=False)

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(DeleteProfile(bot))