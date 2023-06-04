import flet as ft


def main(page: ft.Page):
    def add_pokemon(e):
        page.update()

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.title = "Pokedex"
    page.appbar = ft.AppBar(
        title=ft.Text("Pokedex"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=add_pokemon, bgcolor=ft.colors.WHITE24
    )
    page.add(ft.Text("Body!"))


# flet run main.py -d
ft.app(target=main)
