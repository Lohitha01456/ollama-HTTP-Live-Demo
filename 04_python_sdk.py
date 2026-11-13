from ollama import Client

#connecting our local ollama service

client=Client(
    host="http://127.0.0.1:11434",
    timeout=180
)  

Model="gemma3:1b"

try:
    print(" Sending request to ollama service in python sdk")
    response=client.chat(
        model=Model,
        messages=[
            {
            "role":"user",
            "content":"Explain how large language models work in five simple points."
            }
        ],
    ) 

    print("\nAI response:\n")
    print(response.message.content)

except Exception as error:
    print("\nError:", error)