import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")