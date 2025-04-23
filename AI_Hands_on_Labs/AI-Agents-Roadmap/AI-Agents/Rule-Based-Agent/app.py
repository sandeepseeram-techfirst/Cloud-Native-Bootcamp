"""
Simple Rule-Based AI Agent
Author: Sandeep Seeram
Description: A basic command-line chatbot using if-else rules.
"""

def simple_agent(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm just code, but I'm doing great! 😄"

    elif "weather" in user_input:
        return "I'm not connected to weather services yet, but it's always sunny in the terminal."

    elif "joke" in user_input:
        return "Why did the developer go broke? Because he used up all his cache!"

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day! 👋"

    else:
        return "I'm still learning. Can you try rephrasing that?"

# Entry point
if __name__ == "__main__":
    print("🤖 Simple AI Agent (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Agent: Goodbye! 👋")
            break
        response = simple_agent(user_input)
        print("Agent:", response)
