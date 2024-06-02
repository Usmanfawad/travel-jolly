from fastapi import APIRouter, Depends
from app.controllers.group_controller import get_group_by_id, create_group, update_group, delete_group
from app.schemas.user_group import UserGroupCreate, UserGroupUpdate, UserGroup
from app.dependencies.authDependencies.auth import auth_deps

router = APIRouter()

@router.get("/groups/{id}", response_model=UserGroup)
async def read_group(id: str, current_user: str = Depends(auth_deps)):
    return await get_group_by_id(id)

@router.post("/groups", response_model=UserGroup, dependencies=[Depends(auth_deps)])
async def create_new_group(group: UserGroupCreate):
    return await create_group(group)

@router.put("/groups/{id}", response_model=UserGroup, dependencies=[Depends(auth_deps)])
async def update_existing_group(id: str, group_update: UserGroupUpdate):
    return await update_group(id, group_update)

@router.delete("/groups/{id}", response_model=dict, dependencies=[Depends(auth_deps)])
async def delete_existing_group(id: str):
    await delete_group(id)
    return {"message": "Group deleted successfully"}
