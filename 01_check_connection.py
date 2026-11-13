import requests

#Address of our local ollama server
Base_URL="http://127.0.0.1:11434"

#The AI model we want to use
Model="gemma3:1b"

try:
    #to send the get request to list installed models 
    response = requests.get(
        f"{Base_URL}/api/tags",
        timeout=10
    )
    #check whether the status request is sucess or not
    response.raise_for_status()
    #convert the JSON response into python data
    data=response.json()
    models=[
        model["name"]
        for model in data.get("models",[])
    ]
    print("ollama server is running")
    print("Available models:",models)
    if Model in models:
        print(f"{Model} is ready to use")
    else:
        print(f"please download the model:ollama pull {Model}")
except requests.RequestException as error:
    print("unable to connect to ollama")
    print("Error:",error)
