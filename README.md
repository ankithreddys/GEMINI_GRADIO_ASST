# Gemini Gradio Interface

This project provides a simple Gradio-based interface for interacting with Google's Gemini API. It enables users to input a prompt and receive AI-generated responses in real-time through streaming.

## Features
- Utilizes **Google Gemini** (`gemini-2.0-flash-exp`) for text generation.
- Streams responses dynamically for an interactive experience.
- Provides a clean and user-friendly UI using **Gradio**.
- Uses **Groq API** for additional functionalities (future enhancements).
- Secure API key handling with `.env` file.

## Prerequisites
Make sure you have the following installed:
- Python 3.8+
- `pip` (Python package manager)

## Installation
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/ankithreddys/GEMINI_GRADIO_ASST.git
cd GEMINI_GRADIO_ASST
```

Create a `.env` file in the root directory and add your API keys:
```ini
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
```

## Usage
Run the script to start the Gradio interface:
```bash
python project.py
```

This will launch a web-based UI where you can enter prompts and receive responses from the Gemini model.

## Dependencies
This project requires the following Python libraries:
- `os`
- `requests`
- `google-generativeai`
- `gradio`
- `markdown`
- `groq`
- `dotenv`
- `beautifulsoup4`

You can install them using:
```bash
pip install os requests google-generativeai gradio markdown groq python-dotenv beautifulsoup4
```

## Author
Developed by **Ankith Reddy Subhanpuram**.

