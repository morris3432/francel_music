import flet as ft
import pygame
import os
import asyncio
from mutagen.mp3 import MP3

class Song:
    def __init__(self, filename):
        self.filename = filename
        self.title = os.path.splitext(filename)[0]
        self.duracion = self.get_duracion()

    def get_duracion(self):
        audio = MP3(os.path.join('audios', self.filename))
        return audio.info.length

async def main_play_wg(page: ft.Page):
    page.title = 'Francel Music'
    page.window_min_height=820
    page.window_min_width=1020
    page.theme_mode=ft.ThemeMode.SYSTEM
    page.padding = 20
    title = ft.Text(value='Francel Music', size=30, style='headline1', color=ft.colors.WHITE)

    pygame.mixer.init()
    playlist = [Song(f) for f in os.listdir('audios') if f.endswith('.mp3')]

    def load_song():
        pygame.mixer.music.load(os.path.join('audios', playlist[c_s_i].filename))

    def play_pause(e):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            play_button.icon = ft.icons.PLAY_ARROW
        else:
            if pygame.mixer.music.get_pos() == -1:
                load_song()
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.unpause()
            play_button.icon = ft.icons.PAUSE
        page.update()

    def change_song(delta):
        nonlocal c_s_i
        c_s_i = (c_s_i + delta) % len(playlist)
        load_song()
        pygame.mixer.music.play()
        update_info_song()
        play_button.icon = ft.icons.PAUSE
        page.update()

    def update_info_song():
        song = playlist[c_s_i]
        song_info.value = f'{song.title}'
        duracion.value = format_time(song.duracion)
        prs_bar.value = 0.0
        c_t_t.value = '00:00'
        page.update()

    def format_time(seconds):
        minutos, seconds = divmod(int(seconds), 60)
        return f'{minutos:02d}:{seconds:02d}'

    async def update_progress():
        while True:
            if pygame.mixer.music.get_busy():
                current_time = pygame.mixer.music.get_pos() / 1000  # Convert to seconds
                prs_bar.value = current_time / playlist[c_s_i].duracion
                c_t_t.value = format_time(current_time)
                page.update()
            await asyncio.sleep(1)

    c_s_i = 0
    song_info = ft.Text(size=20, color=ft.colors.WHITE)
    c_t_t = ft.Text(value='00:00', color=ft.colors.WHITE60)
    duracion = ft.Text(value='00:00', color=ft.colors.WHITE60)
    prs_bar = ft.ProgressBar(value=0.0, width=800, color='white', bgcolor='gray')
    play_button = ft.IconButton(icon=ft.icons.PLAY_ARROW, on_click=play_pause, icon_color=ft.colors.WHITE)
    before_button = ft.IconButton(icon=ft.icons.SKIP_PREVIOUS, on_click=lambda _: change_song(-1), icon_color=ft.colors.WHITE)
    after_button = ft.IconButton(icon=ft.icons.SKIP_NEXT, on_click=lambda _: change_song(+1), icon_color=ft.colors.WHITE)

    
    contenedor_wg = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=song_info,
                            padding=ft.padding.only(50)
                        ),
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    c_t_t,
                                    prs_bar,
                                    duracion
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            )
                        ),
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    before_button,
                                    play_button,
                                    after_button
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            padding=ft.padding.only()
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                width=1000,
                height=130,
                border_radius=20,
                gradient=ft.LinearGradient(
                    colors=[ft.colors.BLUE_900, ft.colors.GREY_900, ft.colors.BLACK],
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1)
                )
        )
    
    if playlist:
        load_song()
        update_info_song()
        page.update()
        await update_progress()


