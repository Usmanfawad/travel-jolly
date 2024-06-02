from fastapi import APIRouter
from app.controllers.auth_controller import login
from app.schemas.user import UserCreate
router = APIRouter()

@router.post("/login")
async def login_user(data: UserCreate):
    return await login(data)
