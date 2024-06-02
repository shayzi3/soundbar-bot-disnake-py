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
     
     
     async def new_sound_save(self, guild: Guild, data: list[str]) -> None:
          async with aiosqlite.connect('data/discord.db') as db:
               cursor = await db.execute("SELECT panel FROM server{}".format(guild.id))
               cursor = await cursor.fetchone()
               cursor: list[str] = json.loads(cursor[0])
               
               for link_ in cursor:
                    if link_[1] == data[1]:
                         return False
               
               cursor.append(data)
               
               await db.execute("UPDATE server{} SET panel = ?".format(guild.id), [json.dumps(cursor)])
               await db.commit()
               
               
     async def get_panel(self, guild: Guild) -> list[list[str]]:
          async with aiosqlite.connect('data/discord.db') as db:
               cursor = await db.execute("SELECT panel FROM server{}".format(guild.id))
               cursor = await cursor.fetchone()
               cursor: list[list[str]] = json.loads(cursor[0])
               
               return cursor
          
          
     async def panel_save(self, guild: Guild, panel: list[list[str]]) -> None:
          async with aiosqlite.connect('data/discord.db') as db:
               await db.execute("UPDATE server{} SET panel = ?".format(guild.id), [json.dumps(panel)])
               await db.commit()
               