
from disnake import Guild

from database.database_ import DatabaseCommands


class FuncsForEditPanel:
     def __init__(self) -> None:
          self.base = DatabaseCommands()
          
          
     async def check_creator_sound(self, id: int, guild: Guild, link: str, name: str) -> None:
          panel = await self.base.get_panel(guild)
          
          for item in panel:
               if item[1] == link and item[2] == id and item[0] == name:                    
                    panel.remove(item)
                    await self.base.panel_save(guild=guild, panel=panel)
                    
                    return True
          return None