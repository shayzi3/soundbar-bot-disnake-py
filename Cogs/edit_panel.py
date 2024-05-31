

from disnake.ext import commands
from disnake import CmdInter


class EditPanelCog(commands.Cog):
     def __init__(self, bot: commands.Bot) -> None:
          self.bot = bot
          
     
     @commands.slash_command(description='Удвлить/Изменить название звука.')
     async def edit_panel(self, inter: CmdInter) -> None:
          ...