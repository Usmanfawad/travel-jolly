from typing import Optional
from bson import ObjectId
import strawberry
from app.db.session import get_collection
from app.graphql.types.destination_type import DestinationType, DestinationInput

@strawberry.type
class DestinationMutation:
    @strawberry.mutation
    async def create_destination(self, input: DestinationInput) -> DestinationType:
        destinations_collection = get_collection("destinations")
        destination_data = input.__dict__
        result = await destinations_collection.insert_one(destination_data)
        destination_data["_id"] = str(result.inserted_id)
        return DestinationType(**destination_data)
    
    @strawberry.mutation
    async def update_destination(self, id: str, input: DestinationInput) -> Optional[DestinationType]:
        destinations_collection = get_collection("destinations")
        destination_data = input.__dict__
        result = await destinations_collection.update_one({"_id": ObjectId(id)}, {"$set": destination_data})
        
        if result.matched_count:
            destination_data["_id"] = id
            return DestinationType(**destination_data)
        return None
    
    @strawberry.mutation
    async def delete_destination(self, id: str) -> bool:
        destinations_collection = get_collection("destinations")
        result = await destinations_collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0
