from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / 'custom_env_file.env'
load_dotenv(dotenv_path=env_path)

load_dotenv(override=True)

# Access environment variables
api_key = os.getenv("API_KEY")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
debug_mode = os.getenv("DEBUG")

# Print or use the variables
print(f"API Key: {api_key}")
print(f"Database Host: {db_host}")
print(f"Database Port: {db_port}")
print(f"Debug Mode: {debug_mode}")
