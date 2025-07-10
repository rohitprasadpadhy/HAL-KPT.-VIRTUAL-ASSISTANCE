import json
import random

# Load JSON data
with open("intents.json") as file:
    intents = json.load(file)

# Chatbot response logic
def get_response(user_input):
    user_input = user_input.lower()
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return random.choice(intent["responses"])
    return "Sorry, I didn’t get that. Try asking something else."

# Run chatbot in terminal
print("Bot: Hello! I am your FAQ Bot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Bye! Have a nice day.")
        break
    response = get_response(user_input)
    print("Bot:", response)
