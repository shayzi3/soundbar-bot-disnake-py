
import aiofiles


async def read_the_file(name: str = None, arg: str = None) -> str:
     async with aiofiles.open('funcs_help/helps.txt', 'r', encoding='utf-8') as r:
          read_ = await r.read()
          read_ = read_.split('___')
     
     if not arg:
          return read_[0].replace('__', name)
     
     elif arg == 'panel':
          return read_[1]
     
     elif arg == 'new_sound':
          return read_[2]