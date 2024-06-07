from typing import Optional
from bson import ObjectId
import strawberry
from app.db.session import get_collection
from app.graphql.types.activity_type import ActivityType, ActivityInput

@strawberry.type
class ActivityMutation:
    @strawberry.mutation
    async def create_activity(self, input: ActivityInput) -> ActivityType:
        activities_collection = get_collection("activities")
        activity_data = input.__dict__
        result = await activities_collection.insert_one(activity_data)
        activity_data["_id"] = str(result.inserted_id)
        return ActivityType(**activity_data)
    
    @strawberry.mutation
    async def update_activity(self, id: str, input: ActivityInput) -> Optional[ActivityType]:
        activities_collection = get_collection("activities")
        activity_data = input.__dict__
        result = await activities_collection.update_one({"_id": ObjectId(id)}, {"$set": activity_data})
        
        if result.matched_count:
            activity_data["_id"] = id
            return ActivityType(**activity_data)
        return None
    
    @strawberry.mutation
    async def delete_activity(self, id: str) -> bool:
        activities_collection = get_collection("activities")
        result = await activities_collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0
