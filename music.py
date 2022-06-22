from chiharu import *
import discord
from discord.ext import commands
import asyncio
######3
import re
import youtube_dl
import urllib

config = get_json_data("data/config.json")
PREFIX = config["prefix"]
VERSION = config["version"]
LANGUAGE = config["language"]
WEBSITE_DOMAIN = config["website_domain"]
language_data = get_json_data(f"data/music/{LANGUAGE}.json")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
bot.remove_command("help")

class ChiharuMusicSource(discord.FFmpegPCMAudio):
  def __init__(self, original_url: str) -> None:
    FFMPEG_OPTIONS = {"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", "options": "-vn"}
    YDL_OPTIONS = {"format": "bestaudio", "quiet": True, "ignoreerrors": True}
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(original_url, download=False)
      extracted_url = info["formats"][0]["url"]
    super().__init__(extracted_url, **FFMPEG_OPTIONS)


class YoutubeSearch:
  def __init__(self, query: tuple) -> None:
    query = "+".join((urllib.parse.quote(word) for word in query))
    html_result = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}")
    self.result = re.findall(r'watch\?v=(\S{11})', html_result.read().decode())
    self.first_result = self.result[0]

  def id_to_url(self, number_of_ids: int) -> str:
    return [f"https://www.youtube.com/watch?v={id}" for id in self.result[:number_of_ids]] if number_of_ids <= len(self.result) else [f"https://www.youtube.com/watch?v={id}" for id in self.result]


@bot.command()
async def join(ctx):
  author_vc = ctx.author.voice.channel if ctx.author.voice is not None else None
  bot_vc = ctx.voice_client
  if author_vc:
    if not bot_vc:
      await author_vc.connect()
      message_data = HData(language_data["join_a_voice_channel"])
      message_data.replace_var("{CHANNEL}", author_vc.name)
      message_data.replace_var("{AUTHOR}", str(ctx.author))
      await ctx.send(embed=HEmbed(message_data))
    elif bot_vc.channel != author_vc:
      await ctx.send(embed=HEmbed(message_data))
    else:
      await bot_vc.move_to(author_vc)
      message_data = HData(language_data["move_to_a_voice_channel"])
      message_data.replace_var("{CHANNEL}", author_vc.name)
      message_data.replace_var("{AUTHOR}", str(ctx.author))
      await ctx.send(embed=HEmbed(message_data))
  else:
    await ctx.send(embed=HEmbed(language_data["author_not_in_a_voice_channel"]))


@bot.command()
async def leave(ctx):
  if ctx.voice_client is None:
    await ctx.send("I'm not currently in any voice channel!")
  elif ctx.voice_client.channel == ctx.author.voice.channel:
    await ctx.send(f"Left **{ctx.voice_client.channel}**.")
    await ctx.voice_client.disconnect()
  else:
    await ctx.send("We are not currently in the same voice channel!")

@bot.command(aliases=["p"])
async def play(ctx, *args):
  await join(ctx)

  if args:
    if not [i for i in ["http://", "https://"] if i in " ".join(args)]:
      url = YoutubeSearch(args).first_result
    else:
      url = args[0]

    # if str(ctx.guild.id) not in queue_list:
    #   queue_list[str(ctx.guild.id)] = [url]
    # else:
    #   queue_list[str(ctx.guild.id)].append(url)

  # if str(ctx.guild.id) not in queue_status:
  #   queue_status[str(ctx.guild.id)] = {"loop": False}

  def play(error=None):
    source = ChiharuMusicSource(url)
    ctx.voice_client.play(source, after=play)

  # def check(error=None):
  #   if error:
  #     print(error)
  #   elif not ctx.voice_client.is_playing():
  #     if not queue_status[str(ctx.guild.id)]["loop"]:
  #       queue_list[str(ctx.guild.id)].pop(0)
  #     if str(ctx.guild.id) in queue_list and len(queue_list[str(ctx.guild.id)]) > 0:
  #       play()

  play()

# @bot.command()
# async def loop(ctx):
#   if str(ctx.guild.id) not in queue_status:
#     queue_status[str(ctx.guild.id)] = {"loop": True}
#   else:
#     queue_status[str(ctx.guild.id)]["loop"] = not queue_status[str(ctx.guild.id)]["loop"]
#   await ctx.send(queue_status[str(ctx.guild.id)]["loop"])


# @bot.command()
# async def skip(ctx):
#   if queue_status[str(ctx.guild.id)]["loop"]:
#     queue_list[str(ctx.guild.id)].pop(0)
#   ctx.voice_client.stop()


# @bot.command()
# async def queue(ctx):
#   await ctx.send(queue_list[str(ctx.guild.id)])


@bot.command()
async def pause(ctx):
  ctx.voice_client.pause()


# @bot.command()
# async def stop(ctx):
#   del(queue_list[str(ctx.guild.id)])
#   ctx.voice_client.stop()
#   await leave(ctx)


@bot.command()
async def resume(ctx):
  ctx.voice_client.resume()


async def main():
  await bot.load_extension("_initialization.init")

bot.run(get_token())