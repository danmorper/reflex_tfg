import reflex as rx
from prueba.components.chat import chat, action_bar

def index() -> rx.Component:
    """The main app component."""
    return rx.vstack(
        chat(),
        action_bar(),
        padding="2em",
        align_items="center",
        spacing="2",
        background_color="#fff",
        min_height="100vh",
    )

app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="blue",
    ),
)
app.add_page(index)