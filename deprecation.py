# DeprecationWarning
# @bot.listen()
# async def on_message(message):
#   if message.author.bot:
#     return
#   if message.author.id in doing_feedback:
#     feedback_data = get_data("data/feedback.json")
#     user_feedback = {
#       "recommender_id": message.author.id,
#       "anonymously_sent": False,
#       "content": message.content
#     }
#     feedback_data.append(user_feedback)
#     save_data("data/feedback_data.json", feedback_data)
#     await message.delete()
#     doing_feedback.remove(message.author.id)

# DeprecationWarning
# class FeedbackView(discord.ui.View):
#   @discord.ui.button(label=command_language_data["button_feedback_label"], style=discord.ButtonStyle.gray, emoji="📨")
#   async def feedback(self, interaction, button):
#     if interaction.user != ctx.author:
#       return await interaction.response.send_message(embed=HEmbed(not_author(interaction.user)), ephemeral=True)
#     await interaction.response.edit_message(embed=HEmbed(command_language_data["feedback_confirm"]), view=None)
#     doing_feedback.append(interaction.user.id)
#     await feedback(ctx)