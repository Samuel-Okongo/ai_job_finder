# openai_tools.py
import openai
import os
from dotenv import load_dotenv
load_dotenv()

# Ensure the OpenAI API key is set in the environment variables
OPENAI_API_KEY = os.getenv('OPENAI_AI_KEY')

def get_job_listings(prompt):
    try:
        # Setup API key should already be set via environment variables
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt + "Include URLs for applying to these jobs.",
            max_tokens=250,  # You may adjust the token limit based on your needs
            temperature=0  # Using 0 for deterministic results
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Failed to fetch job listings."
