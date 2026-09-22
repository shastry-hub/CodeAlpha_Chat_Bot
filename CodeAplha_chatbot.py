import random
import time
from datetime import date

responses = {
    "hello": ["Hi! 😊", "Hello there! 👋", "Hey! Nice to see you! 😄"],
    "how are you": ["I'm fine, thanks! 😊", "I'm doing great! 🌟", "All systems are working perfectly! 🤖"],
    "what is your name": ["My name is PyBot. 🤖", "You can call me PyBot! 😊", "I am your Python chatbot. 🐍"],
    "who made you": ["I was created by a student using Python. 🐍", "I was made as a rule-based chatbot project. 📚"],
    "what can you do": ["I can answer questions, tell jokes, and chat with you. 😄", "I can greet you, give advice, tell jokes, and show the date. 🤖"],
    "tell me a joke": ["Why did the computer go to the doctor? Because it had a virus! 😂", "What do computers eat? Microchips! 🤣", "Why was the Python programmer calm? They knew how to handle exceptions! 🐍"],
    "how old are you": ["I don't have a real age. I am a computer program. 🤖", "I don't grow older like humans. 😊"],
    "are you a robot": ["Yes, I am a simple chatbot program. 🤖", "I am a software bot, not a physical robot. 💻"],
    "where are you from": ["I live inside this Python program. 💻", "I come from the world of code! 🌍🐍"],
    "what is the date": [f"Today's date is {date.today().strftime('%d %B %Y')}. 📅", f"It is {date.today().strftime('%A, %d %B %Y')}. 🗓️"],
    "nice to meet you": ["Nice to meet you too! 🤝😊", "The pleasure is mine! 🌟"],
    "i am bored": ["Let's learn something new! 🎮📚", "Try writing a small Python program. 🐍", "How about reading, music, or a new hobby? 🎵"],
    "career advice": ["Choose a field you enjoy and build small projects. 🚀", "Practice your skills and create a portfolio. 💼", "Set one goal and improve every day. 🌟"]
}

def show_help():
    print("\n📋 You can ask me:")
    for question in responses:
        print(" •", question)
    print(" • help")
    print(" • bye\n")

def get_reply(text):
    text = text.lower().strip()
    if text in responses:
        return random.choice(responses[text])
    elif text in ["hi", "hey", "good morning", "good evening"]:
        return random.choice(responses["hello"])
    elif text in ["how r u", "how are u"]:
        return random.choice(responses["how are you"])
    elif text in ["your name", "what's your name"]:
        return random.choice(responses["what is your name"])
    elif text in ["joke", "tell a joke"]:
        return random.choice(responses["tell me a joke"])
    elif text in ["date", "today's date", "todays date"]:
        return random.choice(responses["what is the date"])
    else:
        return random.choice([
            "Sorry, I don't understand. Type 'help'. 🤔",
            "I am still learning! Try a question from 'help'. 😊",
            "That question is not in my list. Type 'help'. 📋"
        ])

def chatbot():
    print("=" * 55)
    print("🤖 Welcome to PyBot - Basic Rule-Based Chatbot")
    print("=" * 55)
    print("Type 'help' to see supported questions.")
    print("Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input == "":
            print("PyBot: Please type something. 😊")
            continue

        if user_input.lower() == "help":
            show_help()
        elif user_input.lower() == "bye":
            print("PyBot: Goodbye! 👋😊")
            print("PyBot: The program will close after 3 second.")
            print("PyBot: Thank you for chatting with me! 🌟")
            time.sleep(3)  # Hidden 3-second wait
            print("Chatbot closed.")
            break
        else:
            print("PyBot:", get_reply(user_input))

if __name__ == "__main__":
    chatbot()
