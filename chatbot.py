import nltk
from nltk.chat.util import Chat, reflections

# Define some basic patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'Great!']),
    (r'what is your name?', ['My name is Chatbot!', 'You can call me Chatbot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a nice day!']),
]

# Create the chatbot using the patterns and reflections
chatbot = Chat(patterns, reflections)

# Start the conversation loop
print("Hello! I'm Chatbot. How can I help you today?")

while True:
    # Get the user's input
    user_input = input('> ')

    # Check if the user wants to quit
    if user_input.lower() in ['bye', 'goodbye']:
        print('Goodbye!')
        break

    # Get the chatbot's response
    response = chatbot.respond(user_input)

    # Print the response
    print(response)
