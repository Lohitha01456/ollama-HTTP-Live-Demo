import requests
import json


# Address of our local Ollama server
Base_Url = "http://127.0.0.1:11434"

# The AI model we want to use
Model = "gemma3:1b"


# The information that we want to send to Ollama
payload = {
    "model": Model,

    "messages": [
        {
            "role": "user",
            "content": "What is Python? Explain in two lines."
        }
    ],

    # True means Ollama will send the response little by little
    "stream": True
}


try:
    print("Streaming AI response:\n")

    # Send our request to Ollama's chat API
    with requests.post(
        f"{Base_Url}/api/chat",
        json=payload,
        stream=True,
        timeout=(5, 180)
    ) as response:

        # Check whether the request was successful
        response.raise_for_status()

        # Read the response line by line
        for line in response.iter_lines():

            # Skip empty lines
            if not line:
                continue

            # Convert the JSON response from text into a Python dictionary
            data = json.loads(line)

            # Check if Ollama returned an error
            if "error" in data:
                raise RuntimeError(data["error"])

            # Get the AI-generated content
            content = data.get("message", {}).get("content", "")

            # Print the AI response without going to a new line
            # flush=True makes the text appear immediately
            print(content, end="", flush=True)

            # If Ollama says the response is finished, stop the loop
            if data.get("done"):
                break

    # This should be outside the for loop
    print("\n\nStreaming completed!")


# Handle possible errors
except (requests.RequestException, ValueError, RuntimeError) as error:
    print("\nError:", error)