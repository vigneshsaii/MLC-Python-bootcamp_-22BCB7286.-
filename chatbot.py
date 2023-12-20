import random

def greet():
    print("Hello! I'm your chatbot. How can I help you today?")

def farewell():
    print("Goodbye! Have a great day.")

def respond_to_greeting():
    responses = ["Hi there!", "Hello!", "Hey!", "Greetings!"]
    print(random.choice(responses))

def handle_user_input(user_input):
    if "how are you" in user_input.lower():
        print("I'm just a computer program, but I'm doing well! Thanks for asking.")
    elif "bye" in user_input.lower() or "goodbye" in user_input.lower():
        farewell()
    else:
        print("I'm not sure how to respond to that. Can you ask me something else?")

def main():
    greet()
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            farewell()
            break

        respond_to_greeting()
        handle_user_input(user_input)

if __name__ == "__main__":
    main()
