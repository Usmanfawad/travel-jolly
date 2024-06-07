from typing import Optional
from bson import ObjectId
import strawberry

from app.db.session import get_collection
from app.graphql.types.activity_type import ActivityType, SuggestionType

@strawberry.type
class ActivityQuery:
    @strawberry.field
    async def activity(self, id: str) -> Optional[ActivityType]:
        activity_collection = get_collection("activities")
        activity = await activity_collection.find_one({"_id": ObjectId(id)})
        
        if activity:
            suggestions = [SuggestionType(name=suggestion["name"], description=suggestion.get("description")) for suggestion in activity.get("suggestions", [])]
            return ActivityType(
                id=str(activity["_id"]),
                destination_id=activity["destination_id"],
                name=activity["name"],
                description=activity["description"],
                suggestions=suggestions
            )
        return None
    
schema = strawberry.Schema(query=ActivityQuery)
