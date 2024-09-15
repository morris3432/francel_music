import flet as ft

def iniciar():
    print('Probando')

def main(page: ft.Page):
    # Configurar el fondo de la página
    page.bgcolor ='#231525'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.padding = 0

    # Crear el contenedor con gradiente y bordes redondeados
    contenedor = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(
                        'Iniciar Sesión',
                        size=30,  # Tamaño del texto
                        weight='w900',
                        color='white'  # Color del texto
                    ),
                    padding=ft.padding.only(60,20)
                ),
                ft.Container(
                    ft.TextField(
                        width=200,
                        height=40,
                        hint_text='Correo electronico',
                        border='underline',
                        color='black',
                        prefix_icon=ft.icons.EMAIL
,                    ),
                    padding=ft.padding.only(60,10)
                ),
                ft.Container(
                    ft.TextField(
                        width=200,
                        height=40,
                        hint_text='Contraseña',
                        border='underline',
                        color='black',
                        prefix_icon=ft.icons.LOCK,
                        password=True
                    ),
                    padding=ft.padding.only(60,5)
                ),
                ft.Container(
                    ft.Checkbox(
                        label='Recordar contraseña',
                        check_color=ft.colors.BLUE_800
                    ),
                    padding=ft.padding.only(80)
                ),
                ft.Container(
                    ft.ElevatedButton(
                        text='Iniciar',
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.PURPLE_900,
                        width=280,
                        on_click=iniciar
                    ),
                    padding=ft.padding.only(20,20)
                ),
                ft.Text('Iniciar sesión con:',
                        text_align='center',
                        width=320),
                ft.Container(
                    ft.Row([
                        ft.IconButton(
                            icon=ft.icons.FACEBOOK,
                            tooltip='Facebook',
                            icon_color='blue',
                            icon_size=30
                        ),
                        ft.IconButton(
                            icon=ft.icons.EMAIL,
                            tooltip='Google',
                            icon_size=30
                        ),
                        ft.IconButton(
                            icon=ft.icons.APPLE,
                            tooltip='Apple',
                            icon_size=30
                        ),
                        
                    ]),
                    padding=ft.padding.only(95)
                ),
                ft.Container(
                    ft.Row(
                        [
                            ft.Text('¿No tienes una cuenta?'),
                            ft.TextButton('Crear Cuenta')
                        ]
                    ),
                    padding=ft.padding.only(30)
                )
                
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        width=320,
        height=500,
        border_radius=20,
        gradient=ft.LinearGradient(
            colors=[ft.colors.PURPLE_900, ft.colors.GREY_900, ft.colors.BLACK],
            begin=ft.Alignment(-1, -1),  # Comienza en la esquina superior izquierda
            end=ft.Alignment(1, 1)       # Termina en la esquina inferior derecha
        )
    )

    # Agregar el contenedor a la página
    page.add(contenedor)

ft.app(target=main)