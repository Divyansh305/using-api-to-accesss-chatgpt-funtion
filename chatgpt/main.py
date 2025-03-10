import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key

def generate_response(user_input):
    """
    Generates a response from OpenAI's language model based on user input.

    Parameters:
    user_input (str): The input string from the user.

    Returns:
    str: The generated response from the chatbot.
    """
    # Call the OpenAI API with user input to get a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    # Extract and return the assistant's reply
    return response.choices[0].message['content']

# Main loop to interact with the chatbot
print("Chatbot initialized! Type 'exit' to end the chat.")
while True:
    # Take user input
    user_input = input("You: ")
    
    # Check for exit condition
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    
    # Generate response from the chatbot
    bot_response = generate_response(user_input)
    
    # Display the response
    print(f"Chatbot: {bot_response}")