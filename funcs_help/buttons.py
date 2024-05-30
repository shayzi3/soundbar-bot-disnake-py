import os

from dotenv import load_dotenv
from disnake import (
     ui,
     ButtonStyle,
     CmdInter
)
from funcs_help.reader import read_the_file

load_dotenv()

class InviteButton(ui.View):
     def __init__(self) -> None:
          super().__init__(timeout=None)
          
          
     @ui.button(label='Add Bot', style=ButtonStyle.link, url=os.getenv('LINK'))
     async def button_help(self, button: ui.Button, inter: CmdInter) -> None:
          self.stop()
          
     @ui.button(label='/audio', style=ButtonStyle.blurple)
     async def button_audio(self, button: ui.Button, inter: CmdInter) -> None:
          text = await read_the_file(arg='audio')
          await inter.send(text, ephemeral=True)
          
          