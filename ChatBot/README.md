# SFBU - Customer Support System

## Introduction
The SFBU Customer Support System is a sophisticated web application designed to enhance user engagement through interactive language processing. It integrates various functionalities, including speech recognition, language modeling, and file handling, to provide a comprehensive customer support experience.

## Design
<table border="1">
  <tr>
    <th>File</th>
    <th>Description</th>
    <th>Internal Processes</th>
  </tr>
  <tr>
    <td>app.py</td>
    <td>Flask-based web application main file.</td>
    <td>
      - Initializes Flask app.<br>
      - Configures upload folders and file types.<br>
      - Sets up routes for web pages and functionalities.<br>
      - Integrates other Python modules for specific features.
    </td>
  </tr>
  <tr>
    <td>llm_Response.py</td>
    <td>Handles language model responses and chatbot functionalities.</td>
    <td>
      - Interfaces with OpenAI API.<br>
      - Manages conversational chains and memory for chatbot.<br>
      - Processes language model responses.
    </td>
  </tr>
  <tr>
    <td>speechRecognation.py</td>
    <td>Focuses on speech recognition and audio processing.</td>
    <td>
      - Utilizes libraries for audio manipulation and speech-to-text.<br>
      - Handles audio file inputs and converts them to text.<br>
      - Integrates with OpenAI for further processing.
    </td>
  </tr>
  <tr>
    <td>vector_and_embedding.py</td>
    <td>Deals with document loading, text processing, and embedding.</td>
    <td>
      - Manages loading of different document types (PDF, URL, YouTube).<br>
      - Processes and splits text for analysis.<br>
      - Handles embedding operations for text data.
    </td>
  </tr>
</table>


## Implementation
To set up and run the SFBU Customer Support System on a local machine, follow these steps:

1. **Environment Setup**: Create a Python virtual environment and activate it:
   ```bash
   python3 -m venv venv
   . venv/bin/activate
   ```

2. **Dependencies**: Update the package manager and install FFmpeg, a suite of libraries and programs for handling video, audio, and other multimedia files and streams:
   ```bash
   sudo apt update && sudo apt install ffmpeg
   ```

3. **Install Python Dependencies**: Install the required Python libraries from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**: Start the Flask application:
   ```bash
   flask run
   ```

## Testing
Upon running the application, the Flask server will host the SFBU Customer Support System on a local server, typically accessible at `http://127.0.0.1:5000/`. The system allows users to interact via text input, file uploads (PDF, URLs, YouTube links), and audio input (speech recognition). The responses and outputs are processed and presented in a user-friendly format, showcasing the system's capabilities in handling and responding to various user queries and inputs.
