import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve the Google API key
google_api_key = os.getenv("GOOGLE_API_KEY")

# Streamlit app
st.title('Nutritionist AI')

if google_api_key:
    st.write("Google API Key is loaded.")
    # Add more Streamlit functionality here
else:
    st.write("Google API Key is not loaded.")



# # test_env.py

# from dotenv import load_dotenv
# import os

# # Load environment variables from the .env file
# load_dotenv()

# # Retrieve the Google API key from the environment variables
# google_api_key = os.getenv("GOOGLE_API_KEY")

# # Check if the API key was loaded correctly
# if google_api_key:
#     print("Google API Key successfully loaded.")
#     print("Google API Key:", google_api_key)
# else:
#     print("Failed to load Google API Key.")