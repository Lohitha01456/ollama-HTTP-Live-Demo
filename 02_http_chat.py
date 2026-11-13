import requests

#Address of our local ollama server
Base_URL="http://127.0.0.1:11434"

#The AI model we want to use
Model="gemma3:1b"

#The information that we want to send to ollama
payload={
    "model": Model,
    "messages":[
        {"role":"user",
         "content": "Explain what an API is with one simple example."}
    ],
    "stream":True
}
try:
    print("sending request to ollama server...")

    response=requests.post(
        f"{Base_URL}/api/chat",
        json=payload,
        timeout=(5,180)
    )
    response.raise_for_status()

    #Read the comple JSON response
    data=response.json()

    #Extract the ai-generated text
    answer=data["message"]["content"]

    print("\nAI Response:\n")
    print(answer)

except requests.RequestException as error:
    print("HTTP request failed:",error)