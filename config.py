import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env into environment

AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_KEY = os.getenv("AZURE_API_KEY")

if not AZURE_ENDPOINT or not AZURE_KEY:
    raise EnvironmentError("Azure Vision credentials not found in .env file")
