import os

from dotenv import load_dotenv
from disnake import (
     ui,
     ButtonStyle,
     CmdInter
)
from funcs_help.reader import read_the_file
load_dotenv()


class WebSites(ui.View):
     def __init__(self) -> None:
          super().__init__(timeout=None)
          
     @ui.button(label='Zvukogram', style=ButtonStyle.link, url='https://zvukogram.com/')
     async def zvukogram(self, button: ui.Button, inter: CmdInter) -> None:
          await inter.response.defer()
          await inter.delete_original_response()
          
     @ui.button(label='Alexbruni', style=ButtonStyle.link, url='https://alexbruni.ru/afx/sound/sounds-from-memes')
     async def alexbruni(self, button: ui.Button, inter: CmdInter) -> None:
          await inter.response.defer()
          await inter.delete_original_response()
          
          

class InviteButton(ui.View):
     def __init__(self) -> None:
          super().__init__(timeout=None)
          
          
     @ui.button(label='Add Bot', style=ButtonStyle.link, url=os.getenv('LINK'))
     async def button_help(self, button: ui.Button, inter: CmdInter) -> None:
          await inter.response.defer()
          await inter.delete_original_response()
          
          
     @ui.button(label='/panel', style=ButtonStyle.blurple)
     async def button_audio(self, button: ui.Button, inter: CmdInter) -> None:
          text = await read_the_file(arg='panel')
          await inter.send(text, ephemeral=True)
          
          
     @ui.button(label='/new_sound', style=ButtonStyle.red)
     async def button_new_sound(self, button: ui.Button, inter: CmdInter) -> None:
          text = await read_the_file(arg='new_sound')
          
          view = WebSites()
          await inter.send(text, view=view, ephemeral=True)
          
          