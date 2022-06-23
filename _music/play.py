import discord
from chiharu import *
from discord.ext import commands

import youtube_dl
import re
import urllib

class Play(ChiharuCog):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

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


async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Play(bot))