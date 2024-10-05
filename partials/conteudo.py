import flet as ft

class CardItem(ft.UserControl):
    def __init__(self,title:str, descricao:str, url:str, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.descricao = descricao
        self.url = url

    def build(self):
        return ft.Container(
            padding=30,
            border_radius=3,
            bgcolor=ft.colors.ON_INVERSE_SURFACE,
            content=ft.Column(
                controls=[
                    ft.Text(
                        value=self.title,
                        theme_style=ft.TextThemeStyle.LABEL_LARGE
                    ),
                    ft.Text(
                        value=self.descricao,
                    ),
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    value="VER AO VIVO",
                                    theme_style=ft.TextThemeStyle.BODY_LARGE,
                                    color=ft.colors.PRIMARY
                                ),
                                ft.Icon(
                                    name=ft.icons.ARROW_FORWARD_IOS,
                                    color=ft.colors.PRIMARY,
                                )
                            ],
                            tight=True
                        ),
                        url=self.url
                    )
                ]
            )
        )


class ConteudoHeader(ft.UserControl):
    def build(self):
        return ft.Container(
            image_src='images/bg.jpg',
            image_fit=ft.ImageFit.COVER,
            image_repeat=ft.ImageRepeat.NO_REPEAT,
            image_opacity=0.5,
            bgcolor=ft.colors.BACKGROUND,
            margin=ft.margin.only(top=30),
            shadow=ft.BoxShadow(
                color='#0E1013',
                offset=ft.Offset(x=0,y=-60),
                spread_radius=-30,
            ),
            border_radius=16,
            content=ft.ResponsiveRow(
                columns=12,
                vertical_alignment="end",
                controls=[
                    ft.Container(
                        col={'md':12, 'lg':8},
                        padding=50,
                        content=(
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        value="Descubra meu Incrível Portifólio",
                                        theme_style=ft.TextThemeStyle.HEADLINE_LARGE 
                                    ),
                                    ft.Text(
                                        spans=[
                                            ft.TextSpan(
                                                text="<",
                                            ),
                                            ft.TextSpan(
                                                text="code",
                                                style=ft.TextStyle(color=ft.colors.PRIMARY),
                                            ),
                                            ft.TextSpan(
                                                text="> "
                                            ),

                                            ft.TextSpan(
                                                text="Eu desenvolvo aplicativos iOS e Android, softwares para MacOS, Windows e Linux. Além de websites responsivos.",
                                                style=ft.TextStyle(color="white"),
                                            ),

                                            ft.TextSpan(
                                                text=" </",
                                            ),
                                            ft.TextSpan(
                                                text="code",
                                                style=ft.TextStyle(color=ft.colors.PRIMARY),
                                            ),
                                            ft.TextSpan(
                                                text="> "
                                            ),
                                        ],
                                        theme_style=ft.TextThemeStyle.BODY_MEDIUM
                                    ),
                                    ft.ElevatedButton(
                                        bgcolor=ft.colors.PRIMARY,
                                        content=ft.Text(
                                            value="Explore agora",
                                            color="black",
                                            weight="bold",
                                        ),
                                        url='',
                                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
                                    )
                                ],
                                spacing=30,
                                alignment=ft.MainAxisAlignment.CENTER,
                            )
                        ),
                    ),
                    ft.Container(
                        col={'md':12, 'lg':4},
                        content=ft.Image(
                            src='images/face-2.png',
                            #scale=ft.Scale(scale=1.8,alignment=ft.alignment.bottom_center)
                        )
                    )
                ]
            )
        )
    
class ConteudoExperiencia(ft.UserControl):
    def build(self):
        return ft.Container(
            padding=20,
            alignment=ft.alignment.center,
            content=ft.ResponsiveRow(
                columns=12,
                controls=[
                    ft.Text(
                        col={'xs':6, 'md': 3},
                        spans=[
                            ft.TextSpan(
                                text="8  + ",
                                style=ft.TextStyle(
                                    color=ft.colors.PRIMARY,
                                    weight='w900',
                                    size=20,
                                )
                            ),
                            ft.TextSpan(
                                text=" Anos de experiência",
                                style=ft.TextStyle(
                                    color="white",
                                    size=16,
                                )
                            )
                        ]
                    ),
                    ft.Text(
                        col={'xs':6, 'md': 3},
                        spans=[
                            ft.TextSpan(
                                text="30  + ",
                                style=ft.TextStyle(
                                    color=ft.colors.PRIMARY,
                                    weight='w900',
                                    size=20,
                                )
                            ),
                            ft.TextSpan(
                                text=" Projetos concluídos",
                                style=ft.TextStyle(
                                    color="white",
                                    size=16,
                                )
                            )
                        ]
                    ),
                    ft.Text(
                        col={'xs':6, 'md': 3},
                        spans=[
                            ft.TextSpan(
                                text="50  + ",
                                style=ft.TextStyle(
                                    color=ft.colors.PRIMARY,
                                    weight='w900',
                                    size=20,
                                )
                            ),
                            ft.TextSpan(
                                text=" Clientes satisfeitos",
                                style=ft.TextStyle(
                                    color="white",
                                    size=16,
                                )
                            )
                        ]
                    ),
                    ft.Text(
                        col={'xs':6, 'md': 3},
                        spans=[
                            ft.TextSpan(
                                text="4  + ",
                                style=ft.TextStyle(
                                    color=ft.colors.PRIMARY,
                                    weight='w900',
                                    size=20,
                                )
                            ),
                            ft.TextSpan(
                                text=" Linguagens de domínio",
                                style=ft.TextStyle(
                                    color="white",
                                    size=16,
                                )
                            )
                        ]
                    )
                ]
            )
        )

class ConteudoProjetos(ft.UserControl):
    def build(self):
        return ft.ResponsiveRow(
            controls=[
                CardItem(
                    title="ToDo App",
                    descricao="Aplicativo para gerenciamento de tarefas com integração com banco de dados do SQLite.",
                    url=""
                    ,col={'xs':12, 'md':6, 'lg':4},
                ),
                CardItem(
                    title="Systmi App",
                    descricao="Aplicativo que extraí dados do site Casa dos Dados e disponibiliza um excel com as informações",
                    url="https://youtu.be/jsHshUUARlo?si=f0oeV70pM_2X5NRZ",
                    col={'xs':12, 'md':6, 'lg':4},
                ),
                CardItem(
                    title="Google Maps Extractor",
                    descricao="Aplicativo ligado ao banco de dados Baserow onde extraí dados do Google Maps de forma automática",
                    url="https://youtu.be/IiL0HJn-i_M?si=3hnQCLdfmeqN4Luo",
                    col={'xs':12, 'md':6, 'lg':4},
                ),
                CardItem(
                    title="CvCadastro App",
                    descricao="Aplicativo android que cria e gerencia cadastros de Produtos ou clientes facilitando a vida de empresas!",
                    url="",
                    col={'xs':12, 'md':6, 'lg':4},
                ),
                CardItem(
                    title="Movie SyS App",
                    descricao="Aplicativo Mobile de filmes com a API do TheMovies - Projeto criado para o canal do Youtube chamado @jimmycodeflet",
                    url="https://youtu.be/O1LHedFq0ec?si=Tpx44L9fQJ_brCno",
                    col={'xs':12, 'md':6, 'lg':4},
                )
            ],
            spacing=30,
            run_spacing=30
        )

class Conteudo(ft.UserControl):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.expand = True

    def build(self):
        def sections_title(title:str):
            return ft.Container(
                padding=ft.padding.symmetric(vertical=20),
                content=ft.Text(
                    value=title,
                    theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM
                )
            )
        
        return ft.Container(
            bgcolor=ft.colors.BACKGROUND,
            padding=20,
            border_radius=16,
            content=ft.Column(
                scroll="hidden",
                controls=[
                    ConteudoHeader(),
                    ConteudoExperiencia(),
                    sections_title(title="Projetos"),
                    ConteudoProjetos()
                ]
            )
        )