import flet as ft


def home_page(page: ft.Page):
    text = ft.Text("Hello, User!")

    def on_click(e):
        text.value = "You clicked the button!"
        page.update()

    def on_click_2(e):
        text.value = "You clicked the button2!"
        page.update()

    def on_click_3(e):
        text.value = "You clicked the button3!"
        page.update()

    return [
        text,
        ft.FilledButton("Enter the main Page", on_click=lambda e: page.push_route("/main")),
        ft.FilledButton("About this app", on_click=on_click_2),
        ft.FilledButton("About the maker", on_click=on_click_3),
    ]


def main_page(page: ft.Page):
    return [
        ft.Text("Hello, User!"),
        ft.Text("xxxxxxxxxxx"),
        ft.FilledButton("back to home", on_click=lambda e: page.push_route("/")),
    ]


def main(page: ft.Page):
    page.title = "My App"

    def route_change(e):
        page.controls.clear()

        if page.route == "/main":
            page.add(*main_page(page))
        else:
            page.add(*home_page(page))

        page.update()

    page.on_route_change = route_change

    # 先手动加载一次首页，防止 on_route_change 没有触发
    page.add(*home_page(page))
    page.update()


ft.run(main)