# Create a test.py file
import os
from dotenv import load_dotenv

load_dotenv()

print(f"SAMBANOVA_API_KEY set: {'Yes' if os.getenv('SAMBANOVA_API_KEY') else 'No'}")
print(f"NUGEN_API_KEY set: {'Yes' if os.getenv('NUGEN_API_KEY') else 'No'}")