"""The home page of the app."""

from practice.templates import template

import reflex as rx


@template(route="/", title="Home", image="/noun-animal-6692529.svg")
def index() -> rx.Component:

    return rx.flex(
        rx.hstack(
            rx.text("Dark mode: "),
            rx.color_mode.switch(),
        ),
        # rx.image(src="/noun-animal-6692529.svg", width="100px", height="100px"),
        #Personal Info Section, shows key-in personal information; able to edit.       
        rx.section(
            rx.flex(
                rx.text("個案資料", size="7", weight="regular"),
                rx.image(src="/edit.png", width="18px", height="18px"),
                justify="between",
                width="100%",
            ),
            rx.spacer(spacing="1"),
            rx.flex(
                rx.flex(
                    rx.text("受訪者編碼"),
                    rx.input(type="text", width="175px"),
                    justify="between", 
                    width="100%",
                    margin= "20px 0 0 0",
                ),
                rx.flex(
                    rx.text("受訪者姓名"),
                    rx.input(type="text", width="175px"),
                    justify="between", 
                    width="100%",
                    margin= "20px 0 0 0",
                ),
                rx.flex(
                    rx.text("生理性別"),
                    rx.select(
                        ["男", "女"],
                        placeholder="生理性別",
                        radius="medium",
                        width="175px",
                        is_require="True"),
                    justify="between", 
                    width="100%",
                    margin= "20px 0 0 0",
                ),        
                rx.flex(
                    rx.text("出生日期"),
                    rx.input(type="date", width="175px"),
                    justify="between", 
                    width="100%",
                    margin= "20px 0 0 0",
                ),
                direction="column",
                width="500px",
                padding="0 20px",
            ),
            direction="column",
            padding="20px 30px",
            justify="center",
            align="center",
        ),
        
        #Note Section, able to edit by clicking the textarea
        rx.section(
            rx.flex(
                rx.text("Note", size="7", weight="regular"),
                rx.spacer(spacing="1"),
                rx.text_area(placeholder="Type here...",),

                justify="between",
                width="100%",
                direction="column",
                ),
            padding="20px 30px",
        ),

        #Database Section, link to batabase pages
        rx.section(
            rx.flex(
                rx.text("資料庫", size="7", weight="regular"),
                rx.spacer(spacing="5"),
                rx.hstack(
                    rx.image(src="/undraw_cat.svg", width="250px", heigt="auto"),
                    rx.image(src="/undraw_cat.svg", width="250px", heigt="auto"),
                ),

                justify="between",
                width="100%",
                direction="column",
                ),
            padding="20px 30px",
        ),


        #Uplaod/Download Section, link to pages & able to upload or download files in this section
        rx.section(
            rx.flex(
                rx.text("檔案上傳＆下載", size="7", weight="regular"),
                rx.spacer(spacing="5"),
                rx.flex(
                    rx.link("Upload Page.", href="/upload")
                ),

                justify="between",
                width="100%",
                direction="column",
                ),
            padding="20px 30px",
        ),

        width="100%",
        direction="column",
        
    )
