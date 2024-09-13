import flet as ft

async def main(page: ft.Page):
    page.title = 'Francel Music'
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.padding = 20
    
    # Crear un marco para el menú horizontal
    menu = ft.Row(
        controls=[
            ft.IconButton(icon=ft.icons.HOME, tooltip='Inicio'),
            ft.IconButton(icon=ft.icons.SEARCH, tooltip='Buscar'),
            ft.IconButton(icon=ft.icons.SETTINGS, tooltip='Configuración'),
        ],
        spacing=10,  # Espaciado entre los botones
        alignment=ft.MainAxisAlignment.START,  # Alineación horizontal
        wrap=True,
    )
    
    # Crear el contenido principal
    content = ft.Column(
        controls=[
            ft.Text(value='Francel Music', style='headline1', color=ft.colors.WHITE),
            # Aquí puedes agregar más controles para tu aplicación
        ],
        spacing=20,  # Espaciado entre los controles
        alignment=ft.MainAxisAlignment.CENTER,  # Alineación vertical
    )
    
    # Crear el diseño principal
    page.add(
        ft.Row(
            controls=[
                ft.Container(
                    content,
                    padding=20,
                    width=ft.ContainerWidth.FILL,
                    bgcolor=ft.colors.BLUE_GREY_800,
                    border_radius=10,
                ),
                ft.Container(
                    menu,
                    padding=20,
                    bgcolor=ft.colors.BLUE_GREY_700,
                    border_radius=10,
                    width=ft.ContainerWidth.AUTO,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
        )
    )

ft.app(target=main)
