from dotenv import load_dotenv
from anthropic import Anthropic

#load environment variable
load_dotenv()

#automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()
conversation_history = []

while True:
    user_input = input("User: ")
    
    if user_input.lower() == "quit":
        print("Conversation ended.")
        break
    
    conversation_history.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        messages=conversation_history,
        max_tokens=500
    )

    assistant_response = response.content[0].text
    print(f"Assistant: {assistant_response}")
    conversation_history.append({"role": "assistant", "content": assistant_response})
