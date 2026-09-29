import flet as ft
import os

IMG_PATH = os.path.expanduser("~/Desktop/Carbine Lense/resorce/logo.png")
IMG_PATH2 = os.path.expanduser("~/Desktop/Carbine Lense/resorce/school.png")
IMG_PATH3 = os.path.expanduser("~/Desktop/Carbine Lense/resorce/CARBINELense.png")

def home_page(page: ft.Page):
    ft.Text("Carbine Lense", color="black", size=50),
    
    async def go_app(e):
        await page.push_route("/app")

    async def go_info(e):
        await page.push_route("/info")

    async def go_maker(e):
            await page.push_route("/people")

    return [
        ft.Row(
    [
        ft.Image(src=IMG_PATH3, width=60, height=60, border_radius=0),
        ft.Text("Carbine", color="green", size=50),
        ft.Text("Lense", color="blue", size=50),
    ],
    spacing=8
),
        ft.FilledButton("Information",
                        on_click=go_info,
                        bgcolor="#2E4AFF",
                        color="#000000",
                        ),
        ft.FilledButton("About this app",
                        on_click=go_app,
                        bgcolor="#FFFFFF",
                        color="#000000",
                        ),
        ft.FilledButton("About the maker",
                        on_click=go_maker,
                        bgcolor="blue",
                        color="#FFFFFF",
                        ),
    ]


def info(page: ft.Page):
    async def go_home(e):
        await page.push_route("/")

    
    return[
    ft.Column(
    [
        ft.Text("Introduction:", size=67),
        ft.Image(src=IMG_PATH, width=100, height=100, border_radius=8),
        ft.Text("13: Climate changes",size=50, color="green"),
        ft.Text("Due to the IPCC(UN Intergovernmental Panel on Climate Change) and NOAA( National Oceanic and Atmospheric Administration )'s latest authoritative data, the damage caused by carbon footprints to the atmosphere and ecosystems manifests primarily in the following four aspects: "),
        ft.Text("For the atmosphere, in the past 15 years, the total annual greenhouse gas emissions have reached a historic peak, which is approximately 50 billion tons of greenhouse gases(carbon dioxide)released into the atmosphere; this clearly illustrates that the global greenhouse effect is significantly worsening, thereby causing the global average temperature continuing to increase at a rate of approximately 0.2 degree celcius per decade "),
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
        ft.Text("This is an I&S project", size=10),
        ft.FilledButton("back to home", on_click=go_home),
    ],
    spacing=12
    )
    ]


def people(page: ft.Page):
    async def go_home(e):
        await page.push_route("/")

    
    return[
    ft.Column(
    [
        ft.Text("About the maker:", size=40, color="blue"),
        ft.Text("This application is made by two students in Prem International School, ChiangMai, Thailand.",
    size=20,
    width=700,
),
        ft.Image(src=IMG_PATH2, width=500, height=100, border_radius=0),
        ft.FilledButton("back to home", on_click=go_home),
    ],
    spacing=12
    )
    ]


def main(page: ft.Page):
    page.title = "Carbine Lense"

    def route_change(e):
        page.controls.clear()

        if page.route == "/info":
            page.add(*info(page))
        elif page.route == "/app":
            page.add(*app(page))
        elif page.route == "/people":
            page.add(*people(page))
        else:
            page.add(*home_page(page))

        page.update()

    page.on_route_change = route_change

    # 先手动加载首页
    page.add(*home_page(page))
    page.update()


ft.run(main)