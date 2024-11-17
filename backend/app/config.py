import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SAMBANOVA_API_KEY: str = os.getenv("SAMBANOVA_API_KEY")
    SAMBANOVA_BASE_URL: str = "https://api.sambanova.ai/v1"
    NUGEN_API_KEY: str = os.getenv("NUGEN_API_KEY")
    NUGEN_API_URL: str = "https://api.nugen.in"

settings = Settings()