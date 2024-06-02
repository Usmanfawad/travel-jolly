from http.client import HTTPResponse
from fastapi import APIRouter, Depends
from app.controllers.user_controller import get_user_by_id, create_user, update_user, delete_user
from app.schemas.user import UserCreate, UserUpdate, User
from app.dependencies.authDependencies.auth import auth_deps
router = APIRouter()

@router.get("/users/{id}", response_model=User)
async def read_user(id: str):
    return await get_user_by_id(id)

@router.post("/users", response_model=User)
async def create_new_user(user: UserCreate):
    return await create_user(user)

@router.put("/users/{id}", response_model=User)
async def update_existing_user(id: str, user_update: UserUpdate, current_user: str = Depends(auth_deps)):
    if current_user != id:
        return {"status": 401, "message": "Unauthorized"}
    return await update_user(id, user_update)

@router.delete("/users/{id}", response_model=dict)
async def delete_existing_user(id: str, current_user: str = Depends(auth_deps)):
    print("current_user: ", current_user)
    if current_user != id:
        return {"status": 401, "message": "Unauthorized"}
    await delete_user(id)
    return {"message": "User deleted successfully"}
