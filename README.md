# FastGPT: A Lightweight ChatGPT Implementation Using FastHTML

**FastGPT** is a minimalistic ChatGPT implementation built using FastHTML, designed to be fast and lightweight, while providing a seamless experience for users. It connects to the GPT-4o model and supports session-based memory to allow for back-and-forth interactions.

We aim to progressively and iteratively add features to better align with the current state of ChatGPT. This project is open-source, so feel free to contribute by submitting a pull request or forking the repo and building upon it yourself!

**Created by Jack Tol**  
[https://jacktol.net](https://jacktol.net)  
[https://conversationai.io](https://conversationai.io)

## Video Demo

Watch the demo of FastGPT on YouTube:

[![FastGPT Demo](https://img.youtube.com/vi/24aGmm_0mTw/0.jpg)](https://www.youtube.com/watch?v=24aGmm_0mTw)

## FastGPT on HuggingFace

Try out the demo directly on Hugging Face: [FastGPT on Hugging Face](https://huggingface.co/spaces/jacktol/FastGPT)

## Features

- **GPT-4o Model Integration**: Connects to the latest version of OpenAI's GPT-4o model for advanced text-based interactions.
- **Session-Based Memory**: Keeps track of the current conversation, allowing for coherent back-and-forth dialogue.
- **Session Management**: Refreshing the page or pressing the "New Chat" button will terminate the current session and initiate a fresh one.
- **Automatic Markdown Parsing**: Both the home page and model responses support Markdown, allowing for easy formatting and enhanced readability.
- **Dynamic Input Box**: The chat input dynamically grows for better visibility when entering long messages.
- **Lightweight Design**: Built without front-end frameworks, leveraging vanilla CSS for a lightweight, fast user experience.
- **Token-by-Token Streaming**: Responses from the model stream onto the screen in real-time, providing instant feedback.
- **Interaction Management**: Users cannot send a message while the model is still generating a response, ensuring a smooth interaction.
- **"New Chat" Button**: Easily initiate a new session with a simple button click.

## Usage Instructions

1. **Clone the Repo**

   ```
   git clone https://github.com/jack-tol/fastgpt.git
   ```

2. **Set your OpenAI API Key**  
   Ensure your `OPENAI_API_KEY` environment variable is set to your OpenAI API Key.

   ```
   export OPENAI_API_KEY=your-openai-api-key-here
   ```

3. **Install Dependencies**  
   Navigate into the cloned directory and install the required dependencies.

   ```
   pip install -r requirements.txt
   ```

4. **Run the Application**  
   Open up your terminal, `cd` into the directory where the `main.py` file is located, and run the following command:

   ```
   uvicorn main:app --port 8080 --reload
   ```

5. **Start Chatting**  
   Open your browser and navigate to `http://localhost:8080` to start your local ChatGPT experience!

## Contributing

Feel free to contribute to FastGPT by submitting a pull request or creating a fork of the repository. As the project evolves, more features will be added to better align with the capabilities of the ChatGPT platform. Help us make FastGPT even better!
