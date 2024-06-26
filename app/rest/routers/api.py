from fastapi import APIRouter
from app.rest.routers.user_routes import router as user_router
from app.rest.routers.auth_routes import router as auth_router
from app.rest.routers.group_routes import router as group_router
from app.rest.routers.role_routes import router as role_router
from app.rest.routers.trip_routes import router as trip_router
from app.rest.routers.destination_routes import router as destination_router
from app.rest.routers.activity_routes import router as activity_router

router = APIRouter()


def include_api_routes():
    """Include to router all api rest routes"""
    router.include_router(user_router)
    router.include_router(auth_router)
    router.include_router(group_router)
    router.include_router(role_router)
    router.include_router(trip_router)
    router.include_router(destination_router)
    router.include_router(activity_router)
    
include_api_routes()
