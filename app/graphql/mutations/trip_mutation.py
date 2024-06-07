from datetime import datetime
from typing import Optional
from bson import ObjectId
import strawberry
from app.db.session import get_collection
from app.graphql.types.trip_type import TripType, TripInput

@strawberry.type
class TripMutation:
    @strawberry.mutation
    async def create_trip(self, input: TripInput, user_id: str) -> TripType:
        trips_collection = get_collection("trips")
        trip_data = input.__dict__
        trip_data["created_date"] = datetime.utcnow()
        trip_data["user_id"] = user_id
        result = await trips_collection.insert_one(trip_data)
        trip_data["_id"] = str(result.inserted_id)
        return TripType(id=trip_data["_id"],
                        name=trip_data["name"],
                        location=trip_data["location"],
                        description=trip_data["description"],
                        start_date=trip_data["start_date"],
                        end_date=trip_data["end_date"],
                        budget=trip_data.get("budget"),
                        user_id=trip_data["user_id"],
                        created_date=trip_data["created_date"])
    
    @strawberry.mutation
    async def update_trip(self, id: str, input: TripInput) -> Optional[TripType]:
        trips_collection = get_collection("trips")
        trip_data = input.__dict__
        result = await trips_collection.update_one({"_id": ObjectId(id)}, {"$set": trip_data})
        
        if result.matched_count:
            trip_data["_id"] = id
            return TripType(id=id,
                            name=trip_data["name"],
                            location=trip_data["location"],
                            description=trip_data["description"],
                            start_date=trip_data["start_date"],
                            end_date=trip_data["end_date"],
                            budget=trip_data.get("budget"),
                            user_id=None,  # No change to user_id
                            created_date=None)  # No change to created_date
        return None
    
    @strawberry.mutation
    async def delete_trip(self, id: str) -> bool:
        trips_collection = get_collection("trips")
        result = await trips_collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0
