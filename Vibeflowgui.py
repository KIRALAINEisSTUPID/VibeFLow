import flet as ft
from flet import MainAxisAlignment, CrossAxisAlignment








body = ft.Container(
    ft.Stack([
            ft.Image(
                src="images/vs.png",
                opacity=0.5,
            )
        ]
    )
)



def main(Page: ft.Page):
    Page.padding = 0
    Page.title = "Vibeflow"
    Page.window.resizable = False

    Page.vertical_alignment = 'center'
    Page.horizontal_alignment = 'center'

    home_button = ft.IconButton(
        ft.Icons.HOME, bgcolor=ft.Colors.PURPLE, icon_color=ft.Colors.WHITE
    )
    choosen_button = ft.IconButton(
        ft.Icons.FILE_OPEN,bgcolor= ft.Colors.BLUE,icon_color=ft.Colors.WHITE
    )
    vibeflow_folder = ft.IconButton(
        ft.Icons.FOLDER, bgcolor=ft.Colors.ORANGE, icon_color=ft.Colors.WHITE
    )
    download = ft.IconButton(
        ft.Icons.DOWNLOAD, bgcolor=ft.Colors.GREEN, icon_color=ft.Colors.WHITE
    )
    settings = ft.IconButton(
        ft.Icons.SETTINGS, bgcolor=ft.Colors.GREY, icon_color=ft.Colors.WHITE
    )
    vibeflow = ft.Text(
        "VibeFlow",
        color=ft.Colors.PURPLE,
        size=40,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    text = ft.Text(
        "Tiny music player",
        size=30,
        text_align=ft.TextAlign.CENTER
    )

    Page.add(
        body
    )

ft.app(target=main)
