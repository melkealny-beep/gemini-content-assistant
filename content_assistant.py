
import google.generativeai as genai
import os
import argparse

def get_api_key_from_env():
    """Manually reads the .env file to find the GOOGLE_API_KEY."""
    try:
        with open('.env', 'r') as f:
            for line in f:
                if line.strip().startswith('GOOGLE_API_KEY'):
                    parts = line.split('=', 1)
                    if len(parts) > 1:
                        return parts[1].strip().strip('"')
    except FileNotFoundError:
        return None
    return None

def main():
    # --- Configuration --- #
    api_key = get_api_key_from_env()
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in .env file.")
        return

    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        print(f"Error configuring GenAI: {e}")
        return

    # --- Model and Generation Settings --- #
    # Using a model from the verified list
    model = genai.GenerativeModel('models/gemini-pro-latest')
    generation_config = genai.GenerationConfig(
        temperature=0.7,
        top_p=1,
        top_k=1,
        max_output_tokens=2048
    )

    # --- Argument Parsing --- #
    parser = argparse.ArgumentParser(description='Generate content using the Gemini API.')
    parser.add_argument('prompt', type=str, help='The text prompt for content generation.')
    args = parser.parse_args()

    # --- Content Generation --- #
    try:
        print(f"--- Generating content for prompt: '{args.prompt}' ---")
        response = model.generate_content(args.prompt, generation_config=generation_config)
        print("\n--- Generated Content ---")
        print(response.text)
        print("\n--- End of Content ---")

    except Exception as e:
        print(f"An error occurred during content generation: {e}")

if __name__ == '__main__':
    main()
