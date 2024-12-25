import nltk
from nltk.chat.util import Chat, reflections

# Predefined conversation pairs
pairs = [
    ["hello|hi|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you?", ["I'm good, how about you?", "I'm fine, thank you!"]],
    ["what is your name?", ["I'm Chatbot, your AI assistant."]],
    ["bye|goodbye", ["Goodbye!", "See you later!"]],
]

# Reflections for personal pronouns
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "me": "you",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Start conversation
def chatbot_interface():
    print("Chatbot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "quit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I'm not sure how to respond to that.")

chatbot_interface()