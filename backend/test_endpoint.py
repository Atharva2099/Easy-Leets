import requests
from pathlib import Path
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_analyze_endpoint():
    """Test the /api/analyze endpoint with a test image"""
    
    # Check if test image exists
    image_path = Path('test.png')
    if not image_path.exists():
        logger.error("test.png not found. Please run create_test_image.py first")
        return
    
    try:
        # Prepare the files
        files = {
            'file': ('test.png', open(image_path, 'rb'), 'image/png')
        }
        
        # Make the request
        logger.info("Sending request to analyze endpoint...")
        response = requests.post(
            'http://127.0.0.1:8000/api/analyze',
            files=files
        )
        
        # Check response
        if response.status_code == 200:
            logger.info("Request successful!")
            result = response.json()
            
            print("\nAnalysis Result:")
            print("-" * 50)
            print("\nProblem Description (from SambaNova):")
            print(result.get('problem', {}).get('description', 'No description available'))
            
            print("\nSolution (from Nugen):")
            print(result.get('solution', {}).get('code', 'No solution available'))
            
        else:
            logger.error(f"Request failed with status code: {response.status_code}")
            logger.error(f"Error message: {response.text}")
            
    except Exception as e:
        logger.error(f"Test failed: {str(e)}")
    finally:
        # Clean up
        files['file'][1].close()

if __name__ == "__main__":
    test_analyze_endpoint()