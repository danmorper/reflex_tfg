import os
import reflex as rx
from openai import OpenAI

# Set up the OpenAI client
client = OpenAI(
    base_url='http://localhost:11434/v1',  # Local API endpoint
    api_key='ollama',  # Required but unused in this context
)

class QA(rx.Base):
    """A question and answer pair."""
    question: str
    answer: str

DEFAULT_CHATS = {
    "Chat": [],
}

class State(rx.State):
    """The app state."""
    chats: dict[str, list[QA]] = DEFAULT_CHATS
    current_chat = "Chat"
    question: str = ""
    processing: bool = False

    async def process_question(self, form_data: dict[str, str]):
        """Process the user's question."""
        question = form_data["question"]
        if question:
            self.chats[self.current_chat].append(QA(question=question, answer=""))
            self.processing = True
            yield

            # Build the full conversation history
            messages = [{"role": "system", "content": "You are a helpful assistant."}]
            for qa in self.chats[self.current_chat]:
                messages.append({"role": "user", "content": qa.question})
                messages.append({"role": "assistant", "content": qa.answer})

            try:
                # Send the request to the OpenAI client with full history
                response = client.chat.completions.create(
                    model="llama3",
                    messages=messages,
                )
                # Extract the answer from the response
                answer = response.choices[0].message.content # It can't be message.['content']
                print(answer)
                self.chats[self.current_chat][-1].answer = answer
            except Exception as e:
                print(f"Error fetching response: {e}")
                self.chats[self.current_chat][-1].answer = "Sorry, I couldn't fetch a response."

            self.chats = self.chats  # Trigger state update
            self.processing = False
