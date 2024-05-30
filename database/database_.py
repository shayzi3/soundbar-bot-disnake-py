import json

import aiosqlite

from loguru import logger
from disnake import Guild


class DatabaseCommands:
     
     async def create_table_for_new_guild(self, guild: Guild) -> bool:
          async with aiosqlite.connect('data/discord.db') as db:
               await db.execute("""CREATE TABLE IF NOT EXISTS server{}(
                    id INT,
                    once TEXT,
                    panel TEXT
               )""".format(guild.id))
               await db.commit()
               
               cursor = await db.execute("SELECT id FROM server{}".format(guild.id))
               cursor = await cursor.fetchone()
               
               if not cursor:
                    await db.execute("INSERT INTO server{} VALUES(?, ?, ?)".format(guild.id), [guild.id, None, json.dumps([])])
                    await db.commit()
                    
                    logger.debug(f'Table for server: {guild.name}')
                    return True
          return False