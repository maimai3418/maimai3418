"""The KE_enter page."""

from practice.templates import template

import reflex as rx


@template(route="/ke", title="K-SADS-E")
def ke_home() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.flex(
            rx.text("兒童精神科 診斷性會談量表 |DSM-5|", size="7", weight="bold"),
            rx.heading("K-SADS-E Interview DSM-5 Version", size="7", weight="light"),
                 
            direction="column",
            align="center",
            justify="center",
            width="100%",
        ),
        rx.spacer(spacing="2"),
       rx.box(
           rx.text("本會談量表內所有內容之著作權、所有權與智慧財產權，為臺大醫院高淑芬醫師研究室所有或經相關著作者同意合法使用。"),
           rx.text("未經本研究室之同意或授權，任何人不得以任何形式重製、轉載、散佈、引用、變更或出版該內容之全部或局部，亦不得為其他任何違反本研究室著作權之行為。"),
           size="4",
           padding="15px 30px",
       ),
       rx.spacer(spacing="4"),
       rx.form(
           rx.flex(
                rx.flex(
                        rx.text("訪談日期"),
                        rx.input(
                            type="date",
                            is_require="True"
                        ),
                        align="center",
                        justify="between",
                        width="300px",
                ),
                rx.flex(
                        rx.text("訪談人員"),
                        rx.select(
                            ["Amy", "Bob", "Chloe", "Diana", "Ellen"],
                            placeholder="選擇訪談人員",
                                # label="訪談人員",
                            radius="medium",
                            width="126px",
                            is_require="True"
                        ),
                        align="center",
                        justify="between",
                        width="300px",
                ),
                rx.button("開始訪談", name="ke_interview_info", type="submit"),
                    rx.link("info_ke", href="/ke/info"),
                    spacing="3",
                    align="center",  
                    direction="column",
                    width="700px",
            )
       )

        
    )
