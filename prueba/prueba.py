import reflex as rx
from prueba.components.chat import chat, action_bar
#https://www.boe.es/buscar/doc.php?id=BOE-A-1986-24403
def index() -> rx.Component:
    """The main app component."""
    return rx.vstack(
        chat(),
        action_bar(),
        padding="2em",
        align_items="center",
        spacing="2",
        background_color="#gray",
        min_height="100vh",
    )

app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="blue",  # Cambiado a un color predefinido aceptable
    ),
)
app.add_page(index)


# Pregunta: ¿En qué fecha se dice en el texto que se produce una deliberación previa?
# Respuesta GPT: Según el texto, la deliberación previa se produce en el Consejo de Ministros el día 29 de agosto de 1986.
# Texto con respuesta: "EN SU VIRTUD, A PROPUESTA DEL MINISTRO DE ECONOMIA Y HACIENDA, OIDO EL CONSEJO DE ESTADO, Y PREVIA DELIBERACION DEL CONSEJO DE MINISTROS EN SU REUNION DEL DIA 29 DE AGOSTO DE 1986, DISPONGO:"