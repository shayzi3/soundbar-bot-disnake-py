

from disnake import (
     ModalInteraction, 
     TextInputStyle,
     ui
)

from funcs_new_sound.functions import SendRequest
from database.database_ import DatabaseCommands



class ModalNewSound(ui.Modal):
     def __init__(self) -> None:
          components = [
               ui.TextInput(
                    label='Название звука',
                    placeholder='Придумайте название звуку',
                    custom_id='name',
                    style=TextInputStyle.short,
                    max_length=20
               ),
               
               ui.TextInput(
                    label='Ссылка',
                    placeholder='Введите ссылку для скачивания.',
                    custom_id='link',
                    style=TextInputStyle.paragraph,
                    max_length=200
               )
          ]
          self.base = DatabaseCommands()
          
          super().__init__(title='Добавление нового звука.', components=components)
          
          
     async def callback(self, inter: ModalInteraction) -> None:
          await inter.response.defer()
          # Пример рабочей ссылки:
          
          # https://zvukogram.com/index.php?r=site/download&id=43754
          # https://alexbruni.ru/afx/sound_file/zvuk-kak-tebe-moya-popa-37.mp3
          
          values = inter.text_values
          sender = SendRequest(values['link'])
          
          result = await sender.chech_link_from_modal()       
          if result:
               data = [values['name'], values['link'], inter.author.id]
               
               base = await self.base.new_sound_save(guild=inter.guild, data=data)
               if base == False:
                    await inter.send(f'**{inter.author.global_name}**, такой звук уже есть!')
                    return
                         
               await inter.send(f'**{inter.author.global_name}**, сохранил новый звук.', delete_after=60)
                    
          elif result == False:
               await inter.send(
                    f'Красивая картинка! **{inter.author.global_name}**',
                    delete_after=15
               )
                    
          else:
               await inter.send(
                    f'Это мне зачем? **{inter.author.global_name}**',
                    delete_after=15
               )
               
          
          
          
          

          