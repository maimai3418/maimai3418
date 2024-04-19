"""Welcome to Reflex!."""

from practice import styles

# Import all the pages.
from practice.pages import *

import reflex as rx


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App(style=styles.base_style)
