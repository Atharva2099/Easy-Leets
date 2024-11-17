from PIL import Image
import io
import base64

def process_image(image_bytes: bytes) -> str:
    """Convert image bytes to base64 string"""
    try:
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert to RGB if needed
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Save to buffer
        buffer = io.BytesIO()
        image.save(buffer, format='PNG')
        
        # Convert to base64
        return base64.b64encode(buffer.getvalue()).decode()
        
    except Exception as e:
        raise ValueError(f"Failed to process image: {str(e)}")