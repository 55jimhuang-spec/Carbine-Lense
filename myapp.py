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

    async def go_main(e):
        await page.push_route("/main")

    return [
        text,
        ft.FilledButton("Enter the main Page", on_click=go_main),
        ft.FilledButton("About this app", on_click=on_click_2),
        ft.FilledButton("About the maker", on_click=on_click_3),
    ]


def main_page(page: ft.Page):
    async def go_home(e):
        await page.push_route("/")

    return [
        ft.Text("Hello, User!"),
        ft.Text("xxxxxxxxxxx"),
        ft.FilledButton("back to home", on_click=go_home),
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

    # 先手动加载首页
    page.add(*home_page(page))
    page.update()


ft.run(main)