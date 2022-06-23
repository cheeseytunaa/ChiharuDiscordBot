import discord
from chiharu import *
from discord.ext import commands

class Join(ChiharuCog):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  @commands.command()
  async def join(self, ctx: commands.Context) -> None:
    author_vc = ctx.author.voice.channel if ctx.author.voice is not None else None
    bot_vc = ctx.voice_client
    if author_vc:
      if not bot_vc:
        await author_vc.connect()
        message_data = HData(self.bot.language_data["join_a_voice_channel"])
        message_data.replace_var("{CHANNEL}", author_vc.name)
        message_data.replace_var("{AUTHOR}", str(ctx.author))
        await ctx.send(embed=HEmbed(message_data))
      elif bot_vc.channel != author_vc:
        await ctx.send(embed=HEmbed(message_data))
      else:
        await bot_vc.move_to(author_vc)
        message_data = HData(self.bot.language_data["move_to_a_voice_channel"])
        message_data.replace_var("{CHANNEL}", author_vc.name)
        message_data.replace_var("{AUTHOR}", str(ctx.author))
        await ctx.send(embed=HEmbed(message_data))
    else:
      await ctx.send(embed=HEmbed(self.bot.language_data["author_not_in_a_voice_channel"]))


async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Join(bot))