"""The Forecasting Longitudinal ASD Project page."""

from practice.templates import ThemeState, template

import reflex as rx


@template(route="/forecast", title="Forecasting")
def forecasting() -> rx.Component:

    return rx.vstack(
        rx.heading("Forecasting Longitudinal ASD Project", size="7", weight="regular"),
        rx.text("量表、神經心理學測驗 橫向預測"),
        rx.text("量表、神經心理學測驗 縱向預測"),
        rx.text("腦影像 橫向預測"),
        rx.text("腦影像 縱向預測"),
        rx.text("整合性預測"),
    )
