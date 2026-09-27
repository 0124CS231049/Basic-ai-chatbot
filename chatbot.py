
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    
    elif "your name" in user_input:
        return "I am a basic AI chatbot."
    elif "ai" in user_input:
        return "Yes, I am an AI chatbot designed to help you with your queries."
    elif "python" in user_input:
        return "Python is a versatile programming language used for web development, data analysis, artificial intelligence, and more."
    elif "machine learning" in user_input:
        return "Machine learning is a subset of AI that allows systems to learn and improve from experience without being explicitly programmed."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase your question?"
    print("AI Chatbot")
    print("Type 'exit' to end the conversation.")
    
while True:    
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    if user_input.lower() == "exit":
        break
            
     
    
    