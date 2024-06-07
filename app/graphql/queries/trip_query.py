from bson import ObjectId
import strawberry
from typing import Optional
from app.graphql.types.trip_type import TripType
from app.db.session import get_collection

@strawberry.type
class TripQuery:
    @strawberry.field
    async def trip(self, id: str) -> Optional[TripType]:
        trips_collection = get_collection("trips")
        trip_data = await trips_collection.find_one({"_id": ObjectId(id)})
        if trip_data:
            return TripType(id=str(trip_data["_id"]),
                            name=trip_data["name"],
                            location=trip_data["location"],
                            description=trip_data["description"],
                            start_date=trip_data["start_date"],
                            end_date=trip_data["end_date"],
                            budget=trip_data.get("budget"),
                            user_id=trip_data["user_id"],
                            created_date=trip_data["created_date"])
            
        return None

schema = strawberry.Schema(query=TripQuery)
