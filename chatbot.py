from google import genai
from dotenv import load_dotenv

load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

if __name__ == "__main__":
    print("Chatbot Initialized! Type 'quit' to end the session.")
    
    while True:
        user_input = input("You: ")
        
        # if the user wants to exit.
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Gemini: Goodbye!")
            break

        # give response based on users input.
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=user_input
        )
        
        # give the response in test format
        print(f"Gemini: {response.text}")
