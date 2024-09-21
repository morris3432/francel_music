import flet as ft
class UI(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)

        def iniciar(e):
            cuenta="cris"
            psd="12345678"
            # Accede a los valores de los campos de texto
            email=self.correo_field.value
            psw=self.contrasena_field.value
            for i in range(3):
                if email == cuenta and psw==psd:
                    print("Bienvenido")
                    ft.open_file('imicio,py')
                else:
                    print("algo esta mal")
                if i ==3:
                    break

            print(email)
            print(psw)
            
            page.update()
            
        # Crear el contenedor de portada
        self.portada = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text('Imagen o contenido de portada')
                        
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            col=8,  # Ocupa 6 columnas en un sistema de 12 columnas
            padding=ft.padding.all(20),
            bgcolor=ft.colors.BLUE_GREY_900
        )

        self.correo_field = ft.TextField(
            width=220,
            height=40,
            hint_text='Correo electrónico',
            border='underline',
            color='black',
            prefix_icon=ft.icons.EMAIL
            
        )
        
        self.contrasena_field = ft.TextField(
            width=220,
            height=40,
            hint_text='Contraseña',
            border='underline',
            color='black',
            prefix_icon=ft.icons.LOCK,
            password=True
        )

        
        # Crear el contenedor con gradiente y bordes redondeados
        self.contenedor = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            'Iniciar Sesión',
                            size=35,  # Tamaño del texto
                            weight='w900',
                            color='white'  # Color del texto
                        ),
                        padding=ft.padding.only(90, 20)
                    ),
                    ft.Container(
                        content=self.correo_field,
                        padding=ft.padding.only(100, 10)
                    ),
                    ft.Container(
                        content=self.contrasena_field,
                        padding=ft.padding.only(100, 5)
                    ),
                    ft.Container(
                        content=ft.Checkbox(
                            label='Recordar contraseña',
                            check_color=ft.colors.BLUE_800
                        ),
                        padding=ft.padding.only(130)
                    ),
                    ft.Container(
                        content=ft.ElevatedButton(
                            text='Iniciar',
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.GREEN_900,
                            width=370,
                            on_click=iniciar
                        ),
                        padding=ft.padding.only(20, 20)
                    ),
                    ft.Text('Iniciar sesión con:',
                            text_align='center',
                            width=410),
                    ft.Container(
                        content=ft.Row([
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
                        padding=ft.padding.only(135)
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Text('¿No tienes una cuenta?'),
                                ft.TextButton('Crear Cuenta')
                            ]
                        ),
                        padding=ft.padding.only(85)
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            col=4,  # Ocupa 6 columnas en un sistema de 12 columnas
            gradient=ft.LinearGradient(
                colors=[ft.colors.GREEN_900, ft.colors.GREY_900, ft.colors.BLACK],
                begin=ft.Alignment(-1, -1),  # Comienza en la esquina superior izquierda
                end=ft.Alignment(1, 1)       # Termina en la esquina inferior derecha
            )
        )
        
        # Crear el contenedor responsivo que incluye portada y contenedor
        self.container = ft.ResponsiveRow(
            controls=[
                self.portada,
                self.contenedor
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    
    def build(self):
        return self.container

def main(page: ft.Page):
    page.window_min_height = 530
    page.window_max_height = 820
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title="Francel Music"
    # Agregar el contenedor a la página
    page.add(UI(page))

ft.app(target=main)
