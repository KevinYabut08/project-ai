import nltk
from nltk.chat.util import Chat, reflections
from textblob import TextBlob

# Predefined conversation pairs
pairs = [
    ["hello|hi|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you?", ["I'm good, how about you?", "I'm fine, thank you!"]],
    ["what is your name?", ["I'm Chatbot, your AI assistant."]],
    ["bye|goodbye", ["Goodbye!", "See you later!"]],
    ["(.*) your favorite (.*)", ["I don't have favorites, but I can help you find yours!"]],
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

# Spell correction function
def correct_spelling(user_input):
    blob = TextBlob(user_input)
    return str(blob.correct())

# Start conversation
def chatbot_interface():
    print("Chatbot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        if not user_input:
            print("Chatbot: Please say something.")
            continue
        if user_input == "quit":
            print("Chatbot: Goodbye!")
            break
        # Correct spelling
        corrected_input = correct_spelling(user_input)
        if corrected_input != user_input:
            print(f"Chatbot: Did you mean '{corrected_input}'?")
        response = chatbot.respond(corrected_input)
        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I'm not sure how to respond to that.")

chatbot_interface()
