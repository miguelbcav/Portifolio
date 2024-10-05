import flet as ft

class Skills(ft.UserControl):
    def __init__(self, title:str, value:float):
        super().__init__()
        self.title = title
        self.value = value
        self.expand = True

    def build(self):
        percentage = self.value * 100  # Transformar o valor em porcentagem
        
        return ft.Column(
            horizontal_alignment='center',
            controls=[
                ft.Stack(
                    controls=[
                        ft.PieChart(
                            sections=[
                                ft.PieChartSection(
                                    value=self.value,
                                    color=ft.colors.PRIMARY,
                                    radius=5
                                ),
                                ft.PieChartSection(
                                    value=1 - self.value,
                                    color=ft.colors.BLACK26,
                                    radius=5
                                )
                            ],
                            sections_space=0,
                            center_space_color=ft.colors.BLACK12,
                            height=70
                        ),
                        ft.Container(
                            content=ft.Text(
                                f"{int(percentage)}%",  # Exibir o valor correto da porcentagem
                                theme_style=ft.TextThemeStyle.BODY_LARGE
                            ),
                            alignment=ft.alignment.center,
                            height=70
                        )
                    ]
                ),
                ft.Text(
                    value=self.title,
                    theme_style=ft.TextThemeStyle.BODY_LARGE
                )
            ]
        )


class SkillProgressBar(ft.UserControl):
    def __init__(self, title:str, value:float):
        super().__init__()
        self.title = title
        self.value = value


    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                value=self.title,
                                theme_style=ft.TextThemeStyle.BODY_LARGE
                            ),
                            ft.Text(
                                value=f'{self.value * 100}%',
                                theme_style=ft.TextThemeStyle.BODY_MEDIUM
                            )
                        ]
                    ),
                    ft.ProgressBar(
                        value=self.value,
                        color=ft.colors.PRIMARY,
                        bgcolor=ft.colors.BLACK26,
                    ),
                    ft.Divider(
                        height=10,
                        color=ft.colors.BLACK12
                    )
                ]
            )
        )
    