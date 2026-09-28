import flet as ft
import os

IMG_PATH = os.path.expanduser("~/Desktop/Carbine Lense/resorce/logo.png")
IMG_PATH2 = os.path.expanduser("~/Desktop/Carbine Lense/resorce/school.png")

def home_page(page: ft.Page):
    text = ft.Text("Hello, User!")

    def on_click(e):
        text.value = "You clicked the button!"
        page.update()

    def on_click_2(e):
        text.value = "You clicked the button2!"
        page.update()

    async def go_app(e):
        await page.push_route("/app")

    async def go_info(e):
        await page.push_route("/info")

    return [
        text,
        ft.FilledButton("Information", on_click=go_info),
        ft.FilledButton("About this app", on_click=go_app),
        ft.FilledButton("About the maker", on_click=on_click_2),
    ]


def info(page: ft.Page):
    async def go_home(e):
        await page.push_route("/")

    
    return[
    ft.Column(
    [
        ft.Text("About our Mission:", size=67),
        ft.Image(src=IMG_PATH, width=200, height=200, border_radius=8),
        ft.Text("xxxxxxxxxxx"),
        ft.FilledButton("back to home", on_click=go_home),
    ],
    spacing=12
    )
    ]

def app(page: ft.Page):
    async def go_home(e):
        await page.push_route("/")

    
    return[
    ft.Column(
    [
        ft.Text("About this application:", size=40, color="blue"),
        ft.Text(
    "The main purpose of this application is to raise awareness of the effects of "
    "carbon footprint and advocate for people to reduce or resist heavy industry pollution.",
    size=20,
    width=700,
),
        ft.Text("This application is made by two students in Prem International School, ChiangMai, Thailand.", size=10),
        ft.Image(src=IMG_PATH2, width=500, height=100, border_radius=0),
        ft.FilledButton("back to home", on_click=go_home),
    ],
    spacing=12
    )
    ]


def main(page: ft.Page):
    page.title = "My App"

    def route_change(e):
        page.controls.clear()

        if page.route == "/info":
            page.add(*info(page))
        elif page.route == "/app":
            page.add(*app(page))
        else:
            page.add(*home_page(page))

        page.update()

    page.on_route_change = route_change

    # 先手动加载首页
    page.add(*home_page(page))
    page.update()


ft.run(main)