import flet as ft
from partials.sidebar import Sidebar
from partials.conteudo import Conteudo

class AppTheme:
    theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            background='#20202a',
            on_background='#0E1013',
            primary='amber',
            inverse_surface='#2d2d3a',
        ),
        text_theme=ft.TextTheme(
            body_medium=ft.TextStyle(color=ft.colors.with_opacity(opacity=.7,color='white'))
        )
    )

class App:
    def __init__(self, page:ft.Page):
        self.page = page
        self.page.bgcolor = "black"
        self.page.theme = AppTheme.theme
        self.page.theme_mode = ft.ThemeMode.DARK
        self.main()

    def main(self):
        self.sidebar = Sidebar(col={'xs':0, 'md':5, 'lg': 4, "xxl":3})
        self.content = Conteudo(col={'xs':12, 'md':7, 'lg': 8, "xxl":9})

        layout = ft.ResponsiveRow(
            expand=True,
            columns=12,
            controls=[
                self.sidebar,
                self.content
            ],
        )

        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target=App,assets_dir="assets",view=ft.AppView.WEB_BROWSER)