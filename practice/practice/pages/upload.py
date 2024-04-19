"""The upload page."""

from practice.templates import ThemeState, template

import reflex as rx


@template(route="/upload", title="Upload")
def upload() -> rx.Component:

    return rx.vstack(
        rx.heading("Upload", size="8"),
        rx.text(
            "You can upload your files here ",
            size="2",
        ),
        rx.upload(
            rx.text(
                "Drag and drop files here or click to select files"
            ),
            id="my_upload",
            border="1px dotted rgb(107,99,246)",
            padding="5em",
        ),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/upload.py"),
            size="1",
        ),
        rx.button(
            "Download",
            on_click=rx.download(url="/jellyfish.svg"),
        ),

    )
