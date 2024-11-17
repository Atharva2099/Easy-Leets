from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import Dict, Any
import logging
from services.nugen_service import NugenService
from utils.image_processing import process_image

logger = logging.getLogger(__name__)
router = APIRouter()
nugen_service = NugenService()

@router.post("/solve",
    response_model=Dict[str, Any],
    summary="Analyze image and generate solution",
    description="Process an image of a graph problem and generate Python solution")
async def solve_problem(
    file: UploadFile = File(..., description="Image file containing the graph problem")
):
    """
    Complete pipeline to solve graph problem from image
    
    Parameters:
    - file: Image file to analyze
    
    Returns:
    - Problem analysis and code solution
    """
    try:
        if not file.content_type.startswith('image/'):
            raise HTTPException(
                status_code=400,
                detail=f"File must be an image, got {file.content_type}"
            )

        contents = await file.read()
        base64_image = process_image(contents)
        
        result = await nugen_service.process_image_and_generate_code(base64_image)
        return result
        
    except Exception as e:
        logger.error(f"Problem solving failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))