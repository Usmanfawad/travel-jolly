from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.schemas.destination import DestinationCreate, Destination
from datetime import datetime
from fastapi import HTTPException

async def create_destination(db: AsyncIOMotorDatabase, destination_data: DestinationCreate):
    # Check if trip_id exists in the database
    trip = await db["trips"].find_one({"_id": ObjectId(destination_data.trip_id)})
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    # Validate dates
    if destination_data.start_date >= destination_data.end_date:
        raise HTTPException(status_code=400, detail="Start date must be before end date")
    destination_data.start_date = datetime.combine(destination_data.start_date, datetime.min.time())
    destination_data.end_date = datetime.combine(destination_data.end_date, datetime.min.time())
        
    destination = destination_data.model_dump()
    result = await db["destinations"].insert_one(destination)
    new_destination = await db["destinations"].find_one({"_id": result.inserted_id})
    if new_destination:
        new_destination["_id"] = str(new_destination["_id"])
    return new_destination

async def get_destination_by_id(db: AsyncIOMotorDatabase, destination_id: str):
    destination = await db["destinations"].find_one({"_id": ObjectId(destination_id)})
    if destination:
        destination["_id"] = str(destination["_id"])
    return destination

async def update_destination(db: AsyncIOMotorDatabase, destination_id: str, destination_update: DestinationCreate):
    # Check if trip_id exists in the database
    trip = await db["trips"].find_one({"_id": ObjectId(destination_update.trip_id)})
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    # Validate dates
    if destination_update.start_date >= destination_update.end_date:
        raise HTTPException(status_code=400, detail="Start date must be before end date")

    await db["destinations"].update_one(
        {"_id": ObjectId(destination_id)},
        {"$set": destination_update.dict()}
    )
    updated_destination = await db["destinations"].find_one({"_id": ObjectId(destination_id)})
    if updated_destination:
        updated_destination["_id"] = str(updated_destination["_id"])
    return updated_destination

async def delete_destination(db: AsyncIOMotorDatabase, destination_id: str):
    await db["destinations"].delete_one({"_id": ObjectId(destination_id)})
    return {"message": "Destination deleted successfully"}
