from fastapi import APIRouter
from .login import router as login_router
from .signup import router as signup_router
from .me import router as me_router

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# Include sub-routers for each auth feature
router.include_router(login_router)
router.include_router(signup_router)
router.include_router(me_router)
