"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from components.nav import nav
from components.hero import hero


class State(rx.State):
    """The app state."""

    ...


@rx.page(route="/", title="Landing")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        # nav bar
        nav(),
        hero(),
        class_name="w-full max-w-7xl p-3 space-y-4 mx-auto",
    )


style = {
    "font_family": "Geist",
    "font_size": "16px",
}

app = rx.App(style=style)
