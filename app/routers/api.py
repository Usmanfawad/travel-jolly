from fastapi import APIRouter
from app.routers.user_routes import router as user_router
from app.routers.auth_routes import router as auth_router

router = APIRouter()


def include_api_routes():
    """Include to router all api rest routes"""
    router.include_router(user_router)
    router.include_router(auth_router)
include_api_routes()
