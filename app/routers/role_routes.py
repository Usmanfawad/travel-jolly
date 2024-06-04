from fastapi import APIRouter, Depends, HTTPException
from app.controllers.role_controler import get_role_by_id, create_role, update_role, delete_role
from app.schemas.group_role import RoleCreate, RoleUpdate, Role
from app.dependencies.authDependencies.auth import JWTBearer

router = APIRouter()

@router.get("/roles/{id}", response_model=Role)
async def read_role(id: str, current_user: str = Depends(JWTBearer())):
    return await get_role_by_id(id)

@router.post("/roles", response_model=Role)
async def create_new_role(role: RoleCreate, current_user: str = Depends(JWTBearer())):
    return await create_role(role)

@router.put("/roles/{id}", response_model=Role)
async def update_existing_role(id: str, role_update: RoleUpdate, current_user: str = Depends(JWTBearer())):
    return await update_role(id, role_update)

@router.delete("/roles/{id}", response_model=dict)
async def delete_existing_role(id: str, current_user: str = Depends(JWTBearer())):
    await delete_role(id)
    return {"message": "Role deleted successfully"}
#  curl -X GET "http://localhost:8000/api/roles/665da1dc6cb099b5b7a707d7" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InVzZXIxQGV4YW1wbGUuY29tIiwidXNlcl9pZCI6IjY2NWRhMDkwMTc2ZmRiMzgwMzZhN2Y4MSIsImV4cCI6MTcxNzQ1NTQ3NH0.QIsc0XDNLQT5nkaqbBjkgHsrPjb1In3Y2NNwVtU0oFo" -H "Content-Type: application/json -d {}"
