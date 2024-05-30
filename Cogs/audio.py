
from disnake.ext import commands
from disnake import CmdInter
from disnake.errors import ClientException
from disnake.utils import get
from loguru import logger

from funcs_audio.get_audio_files import FastSoundCommands   
          

class FastSoundCog(commands.Cog):
     def __init__(self, bot: commands.Bot) -> None:
          self.bot = bot
          self.command_ = FastSoundCommands()
          
          logger.info('audio запущен...')
          
          
     @commands.slash_command(description='Воспроизведение рандомного аудио.')
     async def audio(self, inter: CmdInter) -> None:
          user = inter.author.voice
          
          if user:  
               find = await self.command_.find_member_in_voice(
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
                         await inter.send('Воспроизвожу аудио снова...', ephemeral=True, delete_after=10)
                         await self.command_.playing_sound_one(voice)
                         
                         return
                         
                    await inter.send('Воспроизвожу аудио...', ephemeral=True, delete_after=10)
                    await self.command_.playing_sound_one(voice)

                         
          else:
               await inter.send(
                    content=f'**{inter.author.global_name}**, вы не находитесь в voice чате.', 
                    ephemeral=True, 
                    delete_after=10)
          
          
          
def setup(bot: commands.Bot) -> None:
     bot.add_cog(FastSoundCog(bot))