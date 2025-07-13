from fastapi import APIRouter
from .get_score import router as get_score_router
from .enhance import router as enhance_router

router = APIRouter(
    prefix="/prompts",
    tags=["prompts"]
)

router.include_router(get_score_router)
router.include_router(enhance_router)
