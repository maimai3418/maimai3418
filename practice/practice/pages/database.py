"""The database page."""

from practice.templates import template

import reflex as rx


@template(route="/database", title="Database")
def database() -> rx.Component:

    return rx.vstack(
        rx.heading("ASD Behavior and Clinical Database", size="7", weight="regular"),
        rx.text("問卷、量表"),
        rx.text("神經心理學測驗"),
        rx.text("腦影像"),

    )
