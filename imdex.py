import flet as ft
import pygame
import os
from mutagen.mp3 import MP3

class Song:
    def __init__(self,filenmae):
        self.filename= filenmae
        self.title=os.path.splitext(filenmae)[0]
        self.duracion =self.get_duracion()
        
    def get_duracion(self):
        audio=MP3(os.path.join('audios', self.filename))
        return audio.info.length
            
async def main(page: ft.Page):
    page.title = 'Francel Music'
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.padding = 20
    
    # Agregar un título en la página
    title = ft.Text(value='Francel Music', size=30, style='headline1', color=ft.colors.WHITE)
    
    
    pygame.mixer.init()
    playlist=[Song(f) for f in os.listdir ('audios') if f.endswith('.mp3')]
    
    c_s_i=0
    song_info=ft.Text(size=20,color=ft.colors.WHITE)
    c_t_t=ft.Text(value='00:00', color=ft.colors.WHITE60)
    prs_bar= ft.ProgressBar(value=0.0, width=500,color='white',bgcolor='gray')
    play_button=ft.IconButton(icon=ft.icons.PLAY_ARROW, icon_color=ft.colors.WHITE )
   
    page.add(title,c_t_t,prs_bar,play_button)

ft.app(target=main)
