# Reflex Chatbot Application

## Overview

This project is a simple chatbot application built using Reflex. The chatbot interacts with users and generates responses using a local OpenAI API endpoint. The application maintains a conversation history to provide contextual responses and supports basic message input and display functionalities.

## Features

- **Chat Interface**: A user-friendly chat interface for sending and receiving messages.
- **Contextual Responses**: Maintains conversation history to provide context-aware responses.
- **Local OpenAI API Integration**: Uses a local OpenAI API for generating responses.

## Requirements

- Python 3.6 or later
- Reflex
- OpenAI API running on a local server

## Installation

1. **Clone the Repository**:

    ```bash
    git clone <repository_url>
    cd reflex-chatbot
    ```

2. **Create a Virtual Environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:

    ```bash
    reflex run
    ```

    The application will start on ports 3001 (frontend) and 8001 (backend).

## Configuration

### OpenAI API

Ensure that the OpenAI API is running locally on `http://localhost:11434/v1`. No special API key configuration is required for this local setup, but the `api_key` field is needed to satisfy the client initialization.

## Project Structure

- `prueba.py`: The main application file.
- `state.py`: Manages the chatbot's state and handles user input and responses.
- `chat.py`: Contains the components for the chat interface.

## File Descriptions

### `prueba.py`

This is the main application entry point. It sets up the layout of the chatbot interface and initializes the Reflex app.

- **`index` function**: Defines the layout with `chat` and `action_bar` components.
- **`app` object**: Configures the Reflex app with a theme and adds the main page.

### `state.py`

Manages the application state, including handling user input and interacting with the OpenAI API to generate responses.

- **`QA` class**: Represents a question and answer pair.
- **`State` class**: Manages the chat history and current question.
- **`process_question` function**: Handles user input, sends it to the OpenAI API, and updates the chat history with the response.

### `chat.py`

Defines the chat interface components for displaying messages and handling user input.

- **`message` function**: Formats and displays individual messages in the chat.
- **`chat` function**: Lists all messages in the current conversation.
- **`action_bar` function**: Provides an input field for typing and sending messages.

## Usage

1. **Start the Application**:

    ```bash
    reflex run
    ```

2. **Access the Chat Interface**:

    Open a web browser and navigate to `http://localhost:3001`.

3. **Interact with the Chatbot**:

    - Type a message in the input field and click "Send".
    - The chatbot will respond, and the conversation history will be displayed.

## Troubleshooting

- **Ensure the Local API is Running**: Verify that the OpenAI API is running on `http://localhost:11434/v1`.
- **Check Browser Console**: Look for errors in the browser console that might indicate issues with the frontend.
- **Review Server Logs**: Check the logs for errors when making API calls or handling responses.

## Contributing

Contributions are welcome! Please follow the standard GitHub workflow for contributing changes or reporting issues.

## License

This project is licensed under the MIT License.
# reflex_tfg
