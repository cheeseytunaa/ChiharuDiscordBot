import discord
from chiharu import *
from discord.ext import commands

class Feedback(ChiharuCog):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  @commands.command()
  async def feedback(self, ctx: commands.Context) -> None:
    command_language_data = self.bot.language_data["command_feedback"]

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

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Feedback(bot))