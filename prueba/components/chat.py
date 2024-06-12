import reflex as rx

from prueba.state import QA, State

def message(qa: QA) -> rx.Component:
    """A single question/answer message."""
    return rx.box(
        rx.box(
            rx.markdown(qa.question, background_color="lightblue", padding="0.5em", border_radius="5px"),
            text_align="right", 
        ),
        rx.box(
            rx.markdown(qa.answer, background_color="lightgreen", padding="0.5em", border_radius="5px"),
            text_align="left",
            margin_top="0.5em",
        ),
        margin_bottom="1em",
        width="100%",
        color="black",
    )

def chat() -> rx.Component:
    """List all the messages in a single conversation."""
    return rx.box(
        rx.foreach(State.chats[State.current_chat], message),
        padding="1em",
        width="100%",
        max_height="70vh",
        overflow_y="scroll",
        border="1px solid #ccc",
        border_radius="10px",
        background_color="#f9f9f9"
    )

def action_bar() -> rx.Component:
    """The action bar to send a new message."""
    return rx.form(
        rx.hstack(
            rx.input(
                placeholder="Type something...",
                id="question",
                width="100%",
            ),
            rx.button("Send", type="submit"),
        ),
        on_submit=State.process_question,
        reset_on_submit=True,
        margin_top="1em",
    )
