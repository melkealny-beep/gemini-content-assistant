
import os
# Correct, modern import
import google.genai as genai
from dotenv import load_dotenv

load_dotenv()

print("--- Modern Gemini Test (using google.genai) ---")
try:
    # Get API Key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in .env file.")
    else:
        print("API Key found.")

    # Configure the client
    genai.configure(api_key=api_key)

    # Create the model
    print("Initializing model 'gemini-pro'...")
    model = genai.GenerativeModel('gemini-pro')

    # Generate content
    print("Generating content...")
    response = model.generate_content("Test: Say 'Hello World'")

    # Print response
    print("Response received:")
    print(response.text)
    print("--- Test Successful ---")

except Exception as e:
    print("--- Test Failed ---")
    print(f"An error occurred: {e}")
