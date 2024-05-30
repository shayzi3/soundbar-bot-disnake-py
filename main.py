import os

from dotenv import load_dotenv
from disnake.ext import commands
from disnake import Intents
from loguru import logger


# https://zvukogram.com/

load_dotenv()
token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), 
     help_command=None, 
     intents=Intents.all(), 
     test_guilds=[1198187444684734505]
)

@bot.event
async def on_ready() -> None:
     logger.info('Бот запущен.')

     bot.load_extensions('Cogs')
     
if __name__ == '__main__':
     bot.run(token)