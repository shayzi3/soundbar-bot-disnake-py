
from disnake import CmdInter
from disnake.ext import commands
from disnake.utils import get
from loguru import logger

from funcs_audio.get_audio_files import FastSoundCommands


class DisconnectCog(commands.Cog):
     def __init__(self, bot: commands.Bot) -> None:
          self.bot = bot
          self.command_ = FastSoundCommands()
          
          logger.info('disconnect запущен...')
          
          
     @commands.slash_command(description='Отключить бота от голосового чата.')
     async def disconnect(self, inter: CmdInter) -> None:
          find = await self.command_.find_member_in_voice(
               bot=self.bot, 
               guild=inter.guild, 
               id=inter.author.id,
               inter=inter
          )
          
          if find:
               voice = get(self.bot.voice_clients, guild=inter.guild)
               if voice and voice.is_connected():
                    await voice.disconnect()
                    
                    await inter.send(
                         content=f'{inter.author.global_name}, исключил бота из канала {voice.channel}', 
                         delete_after=25)
                    
          elif find == False:
               # Можно вернуть Embed
               await inter.send('Бот не находится в голосовом канале.', ephemeral=True, delete_after=15)
                    

def setup(bot: commands.Bot) -> None:
     bot.add_cog(DisconnectCog(bot))