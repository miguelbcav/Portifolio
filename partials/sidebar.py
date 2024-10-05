import flet as ft
from components.skills import Skills, SkillProgressBar

class SidebarHeader(ft.UserControl):
    def build(self):
        return ft.Container(
            alignment=ft.alignment.center,
            padding=ft.padding.symmetric(vertical=20,horizontal=40),
            content=ft.Column(
                horizontal_alignment='center',
                controls=[
                    ft.Badge(
                        content=ft.Image(
                            src='images/face-1.jpg',
                            border_radius=360,
                            width=100
                        ),
                        bgcolor=ft.colors.PRIMARY,
                        small_size=20,
                        text='✓',
                        text_color="white",
                        text_style=ft.TextStyle(size=20),
                    ),
                    ft.Text("Miguel Cavalcanti",theme_style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Text("Desenvolvedor FullStack",theme_style=ft.TextThemeStyle.BODY_MEDIUM,opacity=0.7),
                ]
            )
        )
    
class SidebarContent(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.expand = True

    def build(self):
        locations = ft.Container(
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                "Residência:",
                                theme_style=ft.TextThemeStyle.BODY_LARGE
                            ),
                            ft.Text(
                                "Brasil",
                                theme_style=ft.TextThemeStyle.BODY_MEDIUM
                            )
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                "Cidade:",
                                theme_style=ft.TextThemeStyle.BODY_LARGE
                            ),
                            ft.Text(
                                "Rio de Janeiro",
                                theme_style=ft.TextThemeStyle.BODY_MEDIUM
                            )
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                "Idade:",
                                theme_style=ft.TextThemeStyle.BODY_LARGE
                            ),
                            ft.Text(
                                "23",
                                theme_style=ft.TextThemeStyle.BODY_MEDIUM
                            )
                        ]
                    ),
                ]
            )
        )

        linguas = ft.Row(
            controls=[
                Skills(title="Português",value=1),
                Skills(title="Inglês",value=0.5),
                Skills(title="Espanhol",value=0.8),
            ]
        )

        skills = ft.Column(
            controls=[
                SkillProgressBar(title="HTML",value=1),
                SkillProgressBar(title="CSS",value=0.7),
                SkillProgressBar(title="Python",value=1),
                SkillProgressBar(title="JavaScript",value=.4),
            ]
        )

        tecnologias = ft.Column(
            spacing=0,
            controls=[
                ft.ListTile(
                    leading=ft.Icon(
                        name=ft.icons.CHECK,
                        color=ft.colors.PRIMARY
                    ),
                    title=ft.Text(
                        value="Flet",
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM
                    )
                ),
                ft.ListTile(
                    leading=ft.Icon(
                        name=ft.icons.CHECK,
                        color=ft.colors.PRIMARY
                    ),
                    title=ft.Text(
                        value="Versionamento com GIT",
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM
                    )
                ),
                ft.ListTile(
                    leading=ft.Icon(
                        name=ft.icons.CHECK,
                        color=ft.colors.PRIMARY
                    ),
                    title=ft.Text(
                        value="Automações, WebScraping",
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM
                    )
                ),
                ft.ListTile(
                    leading=ft.Icon(
                        name=ft.icons.CHECK,
                        color=ft.colors.PRIMARY
                    ),
                    title=ft.Text(
                        value="API , Requests",
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM
                    )
                ),
                ft.ListTile(
                    leading=ft.Icon(
                        name=ft.icons.CHECK,
                        color=ft.colors.PRIMARY
                    ),
                    title=ft.Text(
                        value="Integração Firebase",
                        theme_style=ft.TextThemeStyle.BODY_MEDIUM
                    )
                ),
            ]
        )

        cv = ft.TextButton(
            text="DOWNLOAD CV",
            style=ft.ButtonStyle(color="grey"),
            icon=ft.icons.DOWNLOAD,
            icon_color="grey"
        )

        return ft.Container(
            bgcolor=ft.colors.BLACK12,
            padding=20,
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    locations,
                    ft.Divider(height=30),
                    linguas,
                    ft.Divider(height=30),
                    skills,
                    ft.Divider(height=30),
                    tecnologias,
                    ft.Divider(height=30),
                    cv
                ]
            )
        )
    
class SidebarFooter(ft.UserControl):
    def build(self):
        return ft.Container(
            padding=ft.padding.symmetric(vertical=10),
            #alignment=ft.alignment.center,
            content=ft.Row(
                alignment="center",
                vertical_alignment="center",
                controls=[
                    ft.IconButton(
                        content=ft.Image(
                            src='icons/001-instagram.png',
                            height=15,
                            color="white"
                        ),
                        url='https://www.instagram.com/miguel.bcav/'
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src='icons/002-linkedin.png',
                            height=15,
                            color="white"
                        )
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src='icons/003-github.png',
                            height=15,
                            color="white"
                        )
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src='icons/004-youtube.png',
                            height=15,
                            color="white"
                        ),
                        url='https://www.youtube.com/@jimmycodeflet'
                    )
                ]
            )
        )
        
class Sidebar(ft.UserControl):
    def build(self):
        return ft.Container(
            content=ft.Column(
                #=ft.ScrollMode.ALWAYS,
                controls=[
                    SidebarHeader(),
                    SidebarContent(),
                    SidebarFooter()
                ]
            ),
            expand=True,
            bgcolor=ft.colors.BACKGROUND,
            border_radius=16
        )