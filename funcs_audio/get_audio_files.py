
from typing import Any
from datetime import datetime as dt

from disnake import (
     VoiceClient,
     FFmpegPCMAudio,
     Guild,
     CmdInter
)
from disnake.ext import commands
from disnake.utils import get

from Scripts.memes import get_url



class FastSoundCommands:
          
     async def playing_sound_panel(self, voice: VoiceClient, url: str) -> None:
          FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
          
          if not voice.is_playing():
               source = FFmpegPCMAudio(source=url, executable='ffm/ffmpeg.exe', **FFMPEG_OPTIONS)
               voice.play(source)
               
          else:
               return None
          
          
     async def find_member_in_voice(
          self, 
          bot: commands.Bot, 
          guild: Guild, 
          id: int, 
          inter: CmdInter
     ) -> bool:
          
          bot_voice = get(bot.voice_clients, guild=guild)
          if bot_voice:
               if id not in [i.id for i in bot_voice.channel.members]:
                    await inter.send(
                         content='Вы не можете взаимодействовать с ботом из другого канала.',
                         ephemeral=True,
                         delete_after=15
                    )
                    return None
               return True
          return False
          
          
               
