
from disnake.ext import commands
from disnake import CmdInter
from loguru import logger

from funcs_new_sound.modals import ModalNewSound


class NewSoundCog(commands.Cog):
     def __init__(self, bot: commands.Bot) -> None:
          self.bot = bot
          
          logger.info('new_sound запущен...')
          
     
     @commands.slash_command(description='Добавить новый звук в звуковую панель.')
     async def new_sound(self, inter: CmdInter) -> None:
          await inter.response.send_modal(ModalNewSound())
          
          
def setup(bot: commands.Bot) -> None:
     bot.add_cog(NewSoundCog(bot))
          
     