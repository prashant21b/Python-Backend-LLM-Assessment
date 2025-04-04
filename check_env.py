import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENAI_API_KEY")
print("✅ Value from .env:", key if key else " NOT FOUND")
