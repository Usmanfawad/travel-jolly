from datetime import datetime
from bson import ObjectId
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.rest.schemas.activity import ActivityCreate, ActivityUpdate

async def get_activity_by_id(db: AsyncIOMotorDatabase, activity_id: str):
    activity = await db["activities"].find_one({"_id": ObjectId(activity_id)})
    if activity:
        activity["_id"] = str(activity["_id"])
        return activity
    raise HTTPException(status_code=404, detail="Activity not found")

async def create_activity(db: AsyncIOMotorDatabase, activity_data: ActivityCreate):
    activity = activity_data.dict()
    activity["created_date"] = datetime.combine(datetime.now().date(), datetime.min.time())

    # Ensure destination_id exists in the database
    destination = await db["destinations"].find_one({"_id": ObjectId(activity["destination_id"])})
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")

    result = await db["activities"].insert_one(activity)
    new_activity = await db["activities"].find_one({"_id": result.inserted_id})
    if new_activity:
        new_activity["_id"] = str(new_activity["_id"])
    return new_activity

async def update_activity(db: AsyncIOMotorDatabase, activity_id: str, activity_data: ActivityUpdate):
    update_data = activity_data.dict(exclude_unset=True)
    result = await db["activities"].update_one({"_id": ObjectId(activity_id)}, {"$set": update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Activity not found")
    updated_activity = await db["activities"].find_one({"_id": ObjectId(activity_id)})
    if updated_activity:
        updated_activity["_id"] = str(updated_activity["_id"])
    return updated_activity

async def delete_activity(db: AsyncIOMotorDatabase, activity_id: str):
    result = await db["activities"].delete_one({"_id": ObjectId(activity_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Activity not found")
    return {"message": "Activity deleted successfully"}
