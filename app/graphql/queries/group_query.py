from bson import ObjectId
import strawberry
from typing import Optional
from app.graphql.types.group_type import GroupMemberType, GroupType
from app.db.session import get_collection

@strawberry.type
class GroupQuery:
    @strawberry.field
    async def group(self, id: str) -> Optional[GroupType]:
        groups_collection = get_collection("groups")
        group_data = await groups_collection.find_one({"_id": ObjectId(id)})
        if group_data:
            members = [GroupMemberType(user_id=member["user_id"], role_id=member["role_id"]) for member in group_data["members"]]
            
            return GroupType(id=str(group_data["_id"]),
                             group_name=group_data["group_name"],
                             members=members,
                             trip_ids=group_data["trip_ids"])
        
        return None

schema = strawberry.Schema(query=GroupQuery)
