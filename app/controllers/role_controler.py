from fastapi import HTTPException
from app.db.session import get_db
from app.schemas.group_role import RoleCreate, RoleUpdate

async def get_role_by_id(role_id: str):
    db = get_db()
    role_collection = db.get_collection("roles")
    role_data = await role_collection.find_one({"_id": role_id})
    if role_data is None:
        raise HTTPException(status_code=404, detail="Role not found")
    role_data["_id"] = str(role_data["_id"])
    return role_data

async def create_role(role: RoleCreate):
    db = get_db()
    role_collection = db.get_collection("roles")
    new_role = role.dict()
    result = await role_collection.insert_one(new_role)
    created_role = await role_collection.find_one({"_id": result.inserted_id})
    created_role["_id"] = str(created_role["_id"])
    return created_role

async def update_role(role_id: str, role_update: RoleUpdate):
    db = get_db()
    role_collection = db.get_collection("roles")
    update_data = {k: v for k, v in role_update.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No data provided to update")
    result = await role_collection.update_one({"_id": role_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Role not found")
    updated_role = await role_collection.find_one({"_id": role_id})
    updated_role["_id"] = str(updated_role["_id"])
    return updated_role

async def delete_role(role_id: str):
    db = get_db()
    role_collection = db.get_collection("roles")
    result = await role_collection.delete_one({"_id": role_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Role not found")
    return {"message": "Role deleted successfully"}