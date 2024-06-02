
from datetime import datetime as dt

from disnake import (
     MessageInteraction, 
     ui, 
     SelectOption, 
     CmdInter,
     ButtonStyle,
     User,
     Embed,
     Colour
)
from disnake.ext import commands

from database.database_ import DatabaseCommands
from funcs_edit_panel.comms import FuncsForEditPanel
          


class SelectMenuEditPanel(ui.Select):
     def __init__(self, data: list[list[str]]) -> None:    
          self.edit = FuncsForEditPanel()
                
          options = [SelectOption(label=item[0], value=f'{item[1]},{item[0]}') for item in data]
          super().__init__(placeholder='Выберите звук', options=options)
          
     
     async def callback(self, inter: MessageInteraction) -> None:
          values = inter.values[0].split(',')
          
          result = await self.edit.check_creator_sound(
               id=inter.author.id,
               guild=inter.guild,
               link=values[0],
               name=values[1]
          )

          if result:
               emb = Embed(
                    title=f'Звук {values[1]} удалён',
                    color=Colour.purple(),
                    timestamp=dt.now()
               )
               emb.set_footer(text=f'Удалил {inter.author.global_name}.')
               await inter.send(embed=emb, delete_after=60)
               
          else:
               await inter.send('Вы не являетесь создателем звука.', ephemeral=True, delete_after=15)
          
          
class ShowSelectMenuEditPanel(ui.View):
     def __init__(self, data) -> None:
          super().__init__(timeout=None)
          self.add_item(SelectMenuEditPanel(data))
          