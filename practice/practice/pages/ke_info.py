"""The KE_info page."""

from practice.templates import template

import reflex as rx



@template(route="/ke/info", title="K-SADS-E Personal Info")
def ke_info() -> rx.Component:

    return rx.flex(
        rx.flex(rx.text("K-SADS-E Interview DSM-5 Version", size="7", weight="light"),
                rx.text("中文版DSM-5兒童青少年精神疾病流行病學診斷會談工具", size="5"),
                direction="column",
                align="center",
                width="100%",
        ),
        rx.flex(
            rx.flex(
                rx.text("受訪者編碼"),
                rx.input(type="text", width="175px"),
                justify="between", 
                width="100%",
                margin= "20px 0 0 0",
            ),
            # rx.flex(
            #     rx.text("受訪者日期"),
            #     rx.input(type="text")
            # ),
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
            rx.flex(
                rx.text("學校名稱／年級"),
                rx.input(type="text", width="175px"),
                rx.input(type="text", width="175px"),
                direction="column",
                margin= "20px 0 0 0",
            ),
            rx.flex(
                rx.text("教育程度"),
                rx.text("最高學歷"),
                rx.input(type="text", width="175px"),
                rx.text("教育年數"),
                rx.input(type="text", width="175px"),
                rx.text("職業"),
                rx.input(type="text"),
                direction="column",
                margin= "20px 0 0 0",
            ),
            rx.flex(
                rx.text("父親教育程度"),
                rx.text("最高學歷"),
                rx.input(type="text"),
                rx.text("教育年數"),
                rx.input(type="text"),
                rx.text("職業"),
                rx.input(type="text"),
                direction="column",
                margin= "20px 0 0 0",
            ),
            rx.flex(
                rx.text("母親教育程度"),
                rx.text("最高學歷"),
                rx.input(type="text"),
                rx.text("教育年數"),
                rx.input(type="text"),
                rx.text("職業"),
                rx.input(type="text"),
                direction="column",
                margin= "20px 0 0 0",
            ),
            direction="column",
            width = "500px",
            margin="20px"
        ),
        width="100%",
        direction="column",
        align="center",
    )


@template(route="/ke/menu", title="K-SADS-E Menu")
def ke_menu() -> rx.Component:

    return rx.flex(
        rx.flex(rx.text("K-SADS-E Interview DSM-5 Version", size="7", weight="light"),
                rx.text("中文版DSM-5兒童青少年精神疾病流行病學診斷會談工具", size="5"),
                direction="column",
                align="center",
                width="100%",
        ),
        rx.flex(
            rx.flex(
                rx.text("障礙症"),
                rx.spacer(),
                rx.text("社交溝通障礙／自閉症類群障礙症"),
                rx.spacer(),
                rx.text("注意力不足／過動症"),
                width="100%",
                direction="column",
                justify="between",
                padding="5px",
                height="22px",
            ),
            rx.flex(
                rx.text("篩檢量表"),
                rx.spacer(),
                rx.button("未完成"),
                rx.spacer(),
                rx.button("未完成"),
                width="100%",
                direction="column",
                justify="between",
                padding="5px",
                height="22px",
            ),
            rx.flex(
                rx.text("完整量表"),
                rx.spacer(),
                rx.button("未完成"),
                rx.spacer(),
                rx.button("未完成"),
                width="100%",
                direction="column",
                justify="between",
                padding="5px",
                height="22px",
            ),
            width="100%",
            justify="between",
            align="center",
        ),
        width="100%",
        direction="column",
        align="center",
    )