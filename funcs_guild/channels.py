
from typing import Any
from datetime import datetime as dt

from disnake import Guild, Embed, Colour
from disnake.utils import get


class ChannelsGuild:
     
      async def general_channel(self, guild: Guild, arg: Any = None) -> None:
          emb = Embed(
               colour=Colour.purple(),
               timestamp=dt.now()
          )
          
          text = 'Где-то я уже видел этот сервер. Пропишите команду /panel'
          url = 'https://media.tenor.com/fcRpkFfRMSUAAAAj/raro-darwin.gif'
          if not arg:
               text = 'Ну наконец-то, хоть куда-то добавили.'
               url = 'https://media.tenor.com/IxkZipSdARcAAAAj/happy-dance.gif'
               
          emb.title = text
          emb.set_thumbnail(url=url)
          
          channel = get(guild.text_channels, name='основной')
          if channel:
               await channel.send(embed=emb, delete_after=120)
                    
          else:
               channel = await guild.create_text_channel(name='основной', reason='Чтобы сообщение отправить.')
               await channel.send(embed=emb, delete_after=120)