import random

import aiohttp

from bs4 import BeautifulSoup



async def search_data(url: str) -> BeautifulSoup:
     async with aiohttp.ClientSession() as session:
          async with session.get(url) as response:
               if response.status == 200:
                    soup = BeautifulSoup(await response.text(), 'lxml')
                    return soup
     return None
     


async def parse_data(soup: BeautifulSoup) -> list[list[str]]:
     onetrack = soup.findAll('div', class_='onetrack accordion')
     
     data = []
     for track in onetrack:
          name = track.find('div', class_='waveTitle').text
          time = track.find('div', class_='waveTime waveOff').text
          
          mp = track.find('div', class_='dwdWrap')
          file = mp.find('a').get('href')
          mp3 = 'https://zvukogram.com' + file
          
          data.append([name, time, mp3])
     return data


async def get_url() -> list[str]:
     url = 'https://zvukogram.com/category/zvuki-iz-memov/?ysclid=lwq0rq8tpu869709087'
     search = await search_data(url)
     
     if search:
          parse = await parse_data(search)
     rnd: list[str] = random.choice(parse)
     
     return rnd


async def get_url_once(once: int) -> list[str]:
     once_memes = random.choice([i for i in range(5, 26)])
     once_time = random.choice([i for i in range(30, 300)])
     
     
     