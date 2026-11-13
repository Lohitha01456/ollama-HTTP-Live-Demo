import requests

#Address of our local ollama server
Base_URL="http://127.0.0.1:11434"

#The AI model we want to use
Model="ai-lohitha"

#The information that we want to send to ollama
payload={
    "model": Model,
    "messages":[
        {"role":"user",
         "content": "Explain what an API is with one simple example."}
    ],
    "stream":False
}
try:
    print("connecting to lohithas ai...")

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

    print("\nlohithas'AI Response:\n")
    print(answer)

except requests.RequestException as error:
    print("HTTP request failed:",error)