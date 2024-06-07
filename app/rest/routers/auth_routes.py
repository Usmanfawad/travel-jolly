from fastapi import APIRouter
from app.rest.controllers.auth_controller import login
from app.rest.schemas.user import UserCreate
router = APIRouter()

@router.post("/login")
async def login_user(data: UserCreate):
    return await login(data)
