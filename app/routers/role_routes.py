from fastapi import APIRouter, Depends, HTTPException
from app.controllers.role_controler import get_role_by_id, create_role, update_role, delete_role
from app.schemas.group_role import RoleCreate, RoleUpdate, Role
from app.dependencies.authDependencies.auth import auth_deps

router = APIRouter()

@router.get("/roles/{id}", response_model=Role)
async def read_role(id: str, current_user: str = Depends(auth_deps)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await get_role_by_id(id)

@router.post("/roles", response_model=Role)
async def create_new_role(role: RoleCreate, current_user: str = Depends(auth_deps)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await create_role(role)

@router.put("/roles/{id}", response_model=Role)
async def update_existing_role(id: str, role_update: RoleUpdate, current_user: str = Depends(auth_deps)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await update_role(id, role_update)

@router.delete("/roles/{id}", response_model=dict)
async def delete_existing_role(id: str, current_user: str = Depends(auth_deps)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    await delete_role(id)
    return {"message": "Role deleted successfully"}
