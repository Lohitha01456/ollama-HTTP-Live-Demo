# Ollama HTTP Live Demo

A beginner-friendly Python project demonstrating how to interact with a local AI model using **Ollama**, HTTP APIs, streaming responses, the Python SDK, and a custom Ollama model configuration.

## 🚀 Project Overview

This project shows different ways to communicate with a locally running Ollama model.

The project uses:

- Python
- Ollama
- HTTP API
- Python SDK
- Gemma 3 1B
- Custom `Modelfile`

## 📁 Project Structure

```text
ollama-HTTP-Live-Demo/
│
├── 01_check_connection.py
├── 02_http_chat.py
├── 03_http_stream.py
├── 04_python_sdk.py
├── 05_ai_lohitha.py
├── ModelFile
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔹 Files

### `01_check_connection.py`

Checks whether the local Ollama server is running and accessible.

### `02_http_chat.py`

Demonstrates sending a message to an Ollama model using the HTTP API.

### `03_http_stream.py`

Demonstrates streaming the AI response as it is generated.

### `04_python_sdk.py`

Shows how to interact with Ollama using a Python SDK instead of directly using HTTP requests.

### `05_ai_lohitha.py`

Uses the custom Ollama model created from the `ModelFile`.

### `ModelFile`

Defines a custom Ollama model based on `gemma3:1b`.

It includes:

- Base model configuration
- Temperature setting
- System instructions
- Beginner-friendly AI behavior

### `requirements.txt`

Contains the Python packages required for the project.

## ⚙️ Prerequisites

Install the following before running the project:

1. Python
2. Ollama
3. Git

Make sure Ollama is running on your computer.

Check the Ollama installation with:

```bash
ollama --version
```

Check available models with:

```bash
ollama list
```

## 📦 Install Python Dependencies

Create and activate a virtual environment if needed:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

## 🤖 Download the Model

This project uses:

```text
gemma3:1b
```

Pull the model using:

```bash
ollama pull gemma3:1b
```

## ▶️ Run the Examples

Run the Python files individually:

```bash
python 01_check_connection.py
```

```bash
python 02_http_chat.py
```

```bash
python 03_http_stream.py
```

```bash
python 04_python_sdk.py
```

```bash
python 05_ai_lohitha.py
```

## 🧠 Creating the Custom Model

The `ModelFile` contains the instructions for the custom AI assistant.

Create the model with:

```bash
ollama create ai-lohitha -f ModelFile
```

Then check that it was created:

```bash
ollama list
```

Run the custom model with:

```bash
ollama run ai-lohitha
```

## 🎯 Learning Goals

This project helps beginners understand:

- How local LLMs work
- How to communicate with Ollama
- HTTP API requests
- Chat APIs
- Streaming AI responses
- Python SDK usage
- System prompts
- Custom Ollama models
- Basic prompt engineering

## 👩‍💻 Author

**Lohitha**

GitHub: [Lohitha01456](https://github.com/Lohitha01456)