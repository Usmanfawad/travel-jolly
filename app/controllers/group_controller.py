from fastapi import HTTPException
from app.db.session import get_db
from app.schemas.user_group import GroupCreate, GroupUpdate
from bson import ObjectId

async def get_group_by_id(group_id: str):
    db = get_db()
    group_collection = db.get_collection("groups")
    group_data = await group_collection.find_one({"_id": ObjectId(group_id)})
    if group_data is None:
        raise HTTPException(status_code=404, detail="Group not found")
    
    group_data["_id"] = str(group_data["_id"])
    return group_data

async def create_group(group: GroupCreate):
    db = get_db()
    group_collection = db.get_collection("groups")
    new_group = group.dict(by_alias=True)
    result = await group_collection.insert_one(new_group)
    created_group = await group_collection.find_one({"_id": result.inserted_id})
    created_group["_id"] = str(created_group["_id"])
    return created_group

async def update_group(group_id: str, group_update: GroupUpdate):
    db = get_db()
    group_collection = db.get_collection("groups")
    update_data = {k: v for k, v in group_update.dict(by_alias=True).items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No data provided to update")
    result = await group_collection.update_one({"_id": ObjectId(group_id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Group not found")
    updated_group = await group_collection.find_one({"_id": ObjectId(group_id)})
    updated_group["_id"] = str(updated_group["_id"])
    return updated_group

async def delete_group(group_id: str):
    db = get_db()
    group_collection = db.get_collection("groups")
    result = await group_collection.delete_one({"_id": ObjectId(group_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Group not found")
    return {"message": "Group deleted successfully"}
