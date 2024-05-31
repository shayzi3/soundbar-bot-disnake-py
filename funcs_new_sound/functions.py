
import aiohttp

from aiohttp.client_exceptions import InvalidURL, ClientConnectorCertificateError


class SendRequest:
     def __init__(self, url: str) -> None:
          self.url = url
          
          
     async def chech_link_from_modal(self) -> bool:
          try:
               async with aiohttp.ClientSession() as session:
                    async with session.head(self.url) as response:
                         content_type = response.headers.get('Content-Type')
                         
                         if content_type == 'image/gif':
                              return False
                         
                         elif content_type == 'audio/mpeg':
                              return True
                         
                         else:
                              return None
                         
          except (InvalidURL, ClientConnectorCertificateError) as ex:
               return None
                    
                    