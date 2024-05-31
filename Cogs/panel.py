
from datetime import datetime as dt
from random import choice

from disnake.ext import commands
from disnake import (
     CmdInter, 
     ui, 
     ButtonStyle, 
     MessageInteraction, 
     Embed, 
     Colour)

from disnake.errors import ClientException
from disnake.utils import get
from loguru import logger

from database.database_ import DatabaseCommands
from funcs_audio.get_audio_files import FastSoundCommands




class PanelCog(commands.Cog):
     def __init__(self, bot: commands.Bot) -> None:
          self.bot = bot
          self.base = DatabaseCommands()
          self.cmd = FastSoundCommands()
          
          logger.info('panel запущен...')
          
     
     @commands.slash_command(description='все добавленные звуки.')
     async def panel(self, inter: CmdInter) -> None:
          panel = await self.base.get_panel(guild=inter.guild)
          if panel:
               color = choice([ButtonStyle.red, ButtonStyle.green, ButtonStyle.blurple])
               view = ui.View()
               
               buttons = []
               for items in panel:
                    button = ui.Button(label=items[0], style=color, custom_id=items[1])                    
                    buttons.append(button)
               
               await inter.send('Выберите звук.', delete_after=900, components=buttons)
               
          else:
               await inter.send('В панеле сервера нет звуков.', ephemeral=True, delete_after=15)
        
        
               
     @commands.Cog.listener('on_button_click')
     async def button_sound(self, inter: MessageInteraction) -> None:
          user = inter.author.voice
          url = inter.component.custom_id
          
          
          if inter.component.label in ['/panel', '/new_sound', 'Add Bot', 'Zvukogram', 'Alexbruni']:
               return None
          
          emb = Embed(
               title=f'Звук: {inter.component.label}',
               colour=Colour.purple(),
               timestamp=dt.now()
          )
          emb.set_footer(text=f'Запросил: {inter.author.global_name}')
          
          if user:
               find = await self.cmd.find_member_in_voice(
                    bot=self.bot, 
                    guild=inter.guild, 
                    id=inter.author.id,
                    inter=inter
               )
               
               if find or find == False:
                    try:
                         voice = await user.channel.connect()
                         
                    except ClientException as ex:
                         voice = get(self.bot.voice_clients, guild=inter.guild)
                         await inter.send(embed=emb, delete_after=13)
                         
                         await self.cmd.playing_sound_panel(voice, url)
                         return
                         
                    await inter.send(embed=emb, delete_after=13)
                    await self.cmd.playing_sound_panel(voice, url)

                         
          else:
               await inter.send(
                    content=f'Вы не находитесь в voice чате.', 
                    ephemeral=True, 
                    delete_after=10
               )



def setup(bot: commands.Bot) -> None:
     bot.add_cog(PanelCog(bot))