from fastapi import APIRouter, Depends, HTTPException
from app.controllers.group_controller import get_group_by_id, create_group, update_group, delete_group
from app.schemas.user_group import GroupCreate, GroupUpdate, Group
from app.dependencies.authDependencies.auth import auth_deps

router = APIRouter()

@router.get("/groups/{id}", response_model=Group)
async def read_group(id: str, current_user: str = Depends(auth_deps)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await get_group_by_id(id)

@router.post("/groups", response_model=Group)
async def create_new_group(group: GroupCreate, current_user: str = Depends(auth_deps)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await create_group(group)

@router.put("/groups/{id}", response_model=Group)
async def update_existing_group(id: str, group_update: GroupUpdate, current_user: str = Depends(auth_deps)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await update_group(id, group_update)

@router.delete("/groups/{id}", response_model=dict)
async def delete_existing_group(id: str, current_user: str = Depends(auth_deps)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    await delete_group(id)
    return {"message": "Group deleted successfully"}
