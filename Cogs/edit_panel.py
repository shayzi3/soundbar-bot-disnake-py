

from disnake.ext import commands
from disnake import CmdInter

from funcs_edit_panel.select_menu_ import ShowSelectMenuEditPanel
from database.database_ import DatabaseCommands


class EditPanelCog(commands.Cog):
     def __init__(self, bot: commands.Bot) -> None:
          self.bot = bot
          self.base = DatabaseCommands()
          
     
     @commands.slash_command(description='Удалить звук.')
     async def edit(self, inter: CmdInter) -> None:
          panel = await self.base.get_panel(guild=inter.guild)
          
          view = ShowSelectMenuEditPanel(data=panel)
          await inter.send(view=view, ephemeral=True)
          

def setup(bot: commands.Bot) -> None:
     bot.add_cog(EditPanelCog(bot))