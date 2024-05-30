

from datetime import datetime as dt

from disnake.ext import commands
from disnake import CmdInter, Embed, Colour
from loguru import logger

from funcs_help.reader import read_the_file
from funcs_help.buttons import InviteButton



class CogHelp(commands.Cog):
     def __init__(self, bot: commands.Bot) -> None:
          self.bot = bot
          
          logger.info('help запущен...')
          
     @commands.slash_command(description='Помощь по командам.')
     async def sos(self, inter: CmdInter) -> None:
          file = await read_the_file(name=inter.author.global_name)
          
          emb = Embed(
               description=file,
               timestamp=dt.now(),
               colour=Colour.purple()
          )
          link = 'https://media.tenor.com/TrZcpR0Kde8AAAAj/cat-meme-funny.gif'
          
          emb.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar)
          emb.set_thumbnail(url=link)
          
          view = InviteButton()
          await inter.send(embed=emb, view=view, ephemeral=True)
     
     
def setup(bot: commands.Bot) -> None:
     bot.add_cog(CogHelp(bot))