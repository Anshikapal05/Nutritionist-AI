# test_env.py

from dotenv import load_dotenv
import os

# Add a print statement to check if the script is running
print("Script started.")

# Load environment variables from the .env file
load_dotenv()

# Add a print statement to check if the .env file was loaded
print(".env file loaded.")

# Retrieve the Google API key from the environment variables
google_api_key = os.getenv("GOOGLE_API_KEY")

# Check if the API key was loaded correctly
if google_api_key:
    print("Google API Key successfully loaded.")
    print("Google API Key:", google_api_key)
else:
    print("Failed to load Google API Key.")
