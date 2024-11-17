from services.sambanova_service import SambanovaService
from services.nugen_service import NugenService
import logging

logger = logging.getLogger(__name__)

def get_sambanova_service() -> SambanovaService:
    try:
        return SambanovaService()
    except Exception as e:
        logger.error(f"Failed to initialize SambaNova service: {str(e)}")
        raise

def get_nugen_service() -> NugenService:
    try:
        return NugenService()
    except Exception as e:
        logger.error(f"Failed to initialize Nugen service: {str(e)}")
        raise