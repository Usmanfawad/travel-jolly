from bson import ObjectId
from fastapi import HTTPException
from app.db.session import get_db
from app.schemas.user_group import UserGroupCreate, UserGroupUpdate

async def get_group_by_id(group_id: str):
    db = get_db()
    group_collection = db.get_collection("groups")
    group_data = await group_collection.find_one({"_id": group_id})
    if group_data is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return group_data

async def create_group(group: UserGroupCreate):
    db = get_db()
    group_collection = db.get_collection("groups")
    user_collection = db.get_collection("user")
    new_group = group.dict()

    for user_id in new_group['members']:
        if not await user_collection.find_one({"_id": ObjectId(user_id)}):
            raise HTTPException(status_code=404, detail="Member not found")

    result = await group_collection.insert_one(new_group)
    created_group = await group_collection.find_one({"_id": result.inserted_id})
    return created_group

async def update_group(group_id: str, group_update: UserGroupUpdate, current_user: str):
    db = get_db()
    group_collection = db.get_collection("groups")
    group_data = await group_collection.find_one({"_id": ObjectId(group_id)})

    if group_data:
        raise HTTPException(status_code=404, detail="Group not found")

    is_admin = False
    for member, role in group_data['members']:
        if member == current_user and role == "admin":
            is_admin = True
            break
    if not is_admin:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    update_data = {k: v for k, v in group_update.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No data provided to update")
    result = await group_collection.update_one({"_id": group_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Group not found")
    updated_group = await group_collection.find_one({"_id": group_id})
    return updated_group

async def delete_group(group_id: str, current_user:str):
    db = get_db()
    group_collection = db.get_collection("groups")
    group_data = await group_collection.find_one({"_id": ObjectId(group_id)})

    if group_data:
        raise HTTPException(status_code=404, detail="Group not found")

    is_admin = False
    for member, role in group_data['members']:
        if member == current_user and role == "admin":
            is_admin = True
            break
    if not is_admin:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    result = await group_collection.delete_one({"_id": group_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Group not found")
