

from disnake.ext import commands
from disnake import Guild
from disnake.utils import get
from loguru import logger

from database.database_ import DatabaseCommands
from funcs_guild.channels import ChannelsGuild


class GuildCog(commands.Cog):
     def __init__(self, bot: commands.Bot) -> None:
          self.bot = bot
          self.data_base = DatabaseCommands()
          self.sound = ChannelsGuild()
          
          logger.info('guild запущен...')
          
          
     @commands.Cog.listener()
     async def on_guild_join(self, guild: Guild) -> None:
          logger.info(f'Bot add on guild: {guild.name}')
          
          result = await self.data_base.create_table_for_new_guild(guild)
          if result:
               await self.sound.general_channel(guild)
               
          else:
               await self.sound.general_channel(guild, arg=1)
          
          
     @commands.Cog.listener()
     async def on_guild_remove(self, guild: Guild) -> None:
          logger.info(f'Bot has been kicked from server {guild.name}')
          
          
          
          
def setup(bot: commands.Bot) -> None:
     bot.add_cog(GuildCog(bot))