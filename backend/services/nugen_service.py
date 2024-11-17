import requests
import logging
import json
from typing import Dict, Any, Optional
from app.config import settings

logger = logging.getLogger(__name__)

class NugenService:
    def __init__(self):
        if not settings.NUGEN_API_KEY:
            raise ValueError("NUGEN_API_KEY is not set in environment")
            
        self.base_url = "https://api.nugen.in"
        self.headers = {
            "Authorization": f"Bearer {settings.NUGEN_API_KEY}",
            "Content-Type": "application/json"
        }
        logger.info("Initialized Nugen service")

    async def process_image_and_generate_code(self, 
                                            base64_image: str,
                                            vision_prompt: str = "Analyze this graph algorithm problem. Identify nodes, edges, weights, and explain what needs to be implemented.",
                                            code_template: str = "Create an efficient Python solution with proper error handling for this problem:\n\n{problem}\n\nInclude:\n1. Input validation\n2. Time and space complexity analysis\n3. Example usage with the given graph") -> Dict[str, Any]:
        """
        Complete pipeline to analyze image and generate code solution
        
        Parameters:
        - base64_image: Base64 encoded image
        - vision_prompt: Custom prompt for vision analysis
        - code_template: Template for code generation
        
        Returns:
        - Dictionary containing both vision analysis and code solution
        """
        try:
            # Step 1: Analyze image with vision model
            vision_payload = {
                "max_tokens": "2000",
                "messages": [
                    {
                        "content": [
                            {
                                "text": vision_prompt,
                                "type": "text"
                            },
                            {
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                },
                                "type": "image_url"
                            }
                        ],
                        "role": "user"
                    }
                ],
                "model": "llama-v3p2-90b-vision-instruct",
                "prompt_truncate_len": 1500,
                "temperature": 0.7
            }

            vision_response = requests.post(
                f"{self.base_url}/inference/chat_vision",
                json=vision_payload,
                headers=self.headers,
                timeout=30
            )
            
            vision_response.raise_for_status()
            vision_result = vision_response.json()
            
            if "choices" not in vision_result or not vision_result["choices"]:
                raise ValueError("No vision analysis results")
                
            problem_description = vision_result["choices"][0]["message"]["content"]
            
            # Step 2: Generate code solution
            final_prompt = code_template.format(problem=problem_description)
            
            code_payload = {
                "max_tokens": "2000",
                "model": "qwen2p5-coder-32b-instruct",
                "prompt": final_prompt,
                "temperature": 1.0
            }

            code_response = requests.post(
                f"{self.base_url}/inference/completions",
                json=code_payload,
                headers=self.headers,
                timeout=30
            )
            
            code_response.raise_for_status()
            code_result = code_response.json()
            
            if not code_result or "choices" not in code_result or not code_result["choices"]:
                raise ValueError("No code generation results")
            
            # Return combined results
            return {
                "status": "success",
                "vision_analysis": {
                    "description": problem_description,
                    "model": "llama-v3p2-90b-vision-instruct"
                },
                "code_solution": {
                    "code": code_result["choices"][0]["text"],
                    "model": "qwen2p5-coder-32b-instruct",
                    "usage": code_result.get("usage", {})
                }
            }

        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            if hasattr(e, 'response'):
                logger.error(f"Response content: {e.response.text}")
            raise ValueError(f"API request failed: {str(e)}")
        except Exception as e:
            logger.error(f"Pipeline failed: {str(e)}")
            raise ValueError(f"Pipeline failed: {str(e)}")

    async def health_check(self) -> Dict[str, str]:
        """Check if Nugen API and models are accessible"""
        try:
            # Test completions endpoint
            test_payload = {
                "max_tokens": "10",
                "model": "qwen2p5-coder-32b-instruct",
                "prompt": "Hello",
                "temperature": 1
            }
            
            response = requests.post(
                f"{self.base_url}/inference/completions",
                json=test_payload,
                headers=self.headers,
                timeout=5
            )
            response.raise_for_status()
            
            return {
                "status": "healthy",
                "vision_model": "llama-v3p2-90b-vision-instruct",
                "code_model": "qwen2p5-coder-32b-instruct",
                "completions_endpoint": "working"
            }
        except Exception as e:
            logger.error(f"Health check failed: {str(e)}")
            return {
                "status": "unhealthy",
                "error": str(e)
            }