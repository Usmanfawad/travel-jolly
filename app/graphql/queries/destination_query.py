from typing import Optional
from bson import ObjectId
import strawberry

from app.db.session import get_collection
from app.graphql.types.destination_type import DestinationType, SuggestionType

@strawberry.type
class DestinationQuery:
    @strawberry.field
    async def destination(self, id: str) -> Optional[DestinationType]:
        dest_col = get_collection("destinations")
        dest = await dest_col.find_one({"_id": ObjectId(id)})
        if dest:
            suggestions = [SuggestionType(**suggestion) for suggestion in dest.get("suggestions", [])]
            return DestinationType(
                id=str(dest["_id"]),
                trip_id=dest["trip_id"],
                name=dest["name"],
                description=dest["description"],
                start_date=dest["start_date"],
                end_date=dest["end_date"],
                destination_type=dest["destination_type"],
                suggestions=suggestions
            )
        return None
    
schema = strawberry.Schema(query=DestinationQuery)
