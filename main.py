import flet as ft
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IMG_PATH = os.path.join(BASE_DIR, "Resources", "logo.png")
IMG_PATH2 = os.path.join(BASE_DIR, "Resources", "school.png")
IMG_PATH3 = os.path.join(BASE_DIR, "Resources", "CARBINELense.png")


def home_page(page: ft.Page):
    page.window.height = 250
    page.window.width = 1200
    
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
             ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
        ),
        ft.Row(
            [
                ft.Text("Carbine", color="green", size=50),
                ft.Text("Lense", color="blue", size=50),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
        ),
        ft.Row(
            [
                ft.FilledButton(
                    "Information",
                    on_click=go_info,
                    bgcolor="#2E4AFF",
                    color="#000000",
                ),
                ft.FilledButton(
                    "About this app",
                    on_click=go_app,
                    bgcolor="#FFFFFF",
                    color="#000000",
                ),
                ft.FilledButton(
                    "About the maker",
                    on_click=go_maker,
                    bgcolor="blue",
                    color="#FFFFFF",
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=12,
        ),
    ]


def info(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.window.height = 800
    page.window.width = 1200
    async def go_home(e):
        await page.push_route("/")

    
    return[
    ft.Column(
    [
        
        ft.Text("Introduction:", size=67),
        ft.Column([
            ft.Text("This Project is about the 13th goal in United Nations Sustainable Development Goals:", color="green", size=30),
            ft.Image(src=IMG_PATH, width=100, height=100, border_radius=8),
        ]),
        ft.Text("Climate changes",size=50, color="green"),
        ft.Text("Climate change is squeezing the living space for our health. "),
        ft.Text("Due to the IPCC(UN Intergovernmental Panel on Climate Change) and NOAA( National Oceanic and Atmospheric Administration )'s latest authoritative data, the damage caused by carbon footprints to the atmosphere and ecosystems manifests primarily in the following 2 aspects:"),
        ft.Text("For the atmosphere, in the past 15 years, the total annual greenhouse gas emissions have reached a historic peak, which is approximately 50 billion tons of greenhouse gases(carbon dioxide)released into the atmosphere; this clearly illustrates that the global greenhouse effect is significantly worsening, thereby causing the global average temperature continuing to increase at a rate of approximately 0.2 degree celsius per decade, however don't underestimate this 0.2 temperature rise, it connects to the whole global climate this means it can accumulate an amount of excess heat energy equivalent to millions of nuclear bombs; it is precisely this 0.2 degree rise that has the frequent occurrence of extreme droughts over the past 15 years." ),
        ft.Text("On land, according to IPCC statistics, including iron, energy, and chemical industries, these heavy industries emit more than 40% of global greenhouse gas emissions. Moving away from the theoretical data: Since 2010, heavy industry and deforestation have caused a large amount of CO2, thereby causing some areas to erode due to droughts and heat, thus directly damaging animals' living spaces." ),
        ft.Text("However, the global climate is not just caused by humans; the natural cycles of the natural world can also affect atmospheric temperature and ecosystems in the short term, such as volcanic eruptions and fluctuations in solar radiation; even orbital variation can also impact climate." ),
        ft.Text("Overall, to a great extent, data show that the carbon footprint has caused irreversible damage to the atmosphere and the ecosystem; however, natural cycles and the development of clean technologies(nuclear power, wind energy, water energy) in recent years have slightly mitigated this trend of destruction. This merely highlights the original design intent of our software, which is just to use technology to increase the number of people focusing on carbon emissions, also enhancing the transparency of industrial emissions, thereby achieving the goal of safeguarding the ecosystem."),
        ft.FilledButton("back to home", on_click=go_home,bgcolor="green", color="#ffc800"),
    ],
    spacing=12
    )
    ]

def app(page: ft.Page):
    page.window.height = 300
    page.window.width = 1200
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
    page.window.height = 500
    page.window.width = 1200
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
    page.window.height = 400
    page.window.width = 1200

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