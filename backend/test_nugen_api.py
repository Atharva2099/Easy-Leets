import requests
import os
from dotenv import load_dotenv
import base64

load_dotenv()

def test_vision_api():
    """Test Nugen Vision API directly"""
    
    api_key = os.getenv("NUGEN_API_KEY")
    if not api_key:
        print("Error: NUGEN_API_KEY not found")
        return
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Read test image
    with open('test.png', 'rb') as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
    
    payload = {
        "max_tokens": "2000",
        "messages": [
            {
                "content": [
                    {
                        "text": "Describe this graph problem.",
                        "type": "text"
                    },
                    {
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_data}"
                        },
                        "type": "image_url"
                    }
                ],
                "role": "user"
            }
        ],
        "model": "nugen-flash-vision",
        "prompt_truncate_len": 1500,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(
            "https://api.nugen.in/inference/chat_vision",
            json=payload,
            headers=headers
        )
        print(f"Status Code: {response.status_code}")
        print("Response:", response.json())
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_vision_api()