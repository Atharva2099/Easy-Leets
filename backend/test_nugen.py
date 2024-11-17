import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_nugen_completion():
    """Test Nugen completions API directly"""
    
    api_key = os.getenv("NUGEN_API_KEY")
    if not api_key:
        print("Error: NUGEN_API_KEY not found")
        return
        
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "max_tokens": "2000",
        "model": "qwen2p5-coder-32b-instruct",
        "prompt": "Write a Python function that implements bubble sort",
        "temperature": 1
    }
    
    try:
        response = requests.post(
            "https://api.nugen.in/inference/completions",
            json=payload,
            headers=headers
        )
        print(f"\nStatus Code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_nugen_completion()