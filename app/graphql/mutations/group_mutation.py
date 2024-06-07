from typing import Optional
from bson import ObjectId
import strawberry
from app.db.session import get_collection
from app.graphql.types.group_type import GroupType, GroupInput, GroupMemberType

@strawberry.type
class GroupMutation:
    @strawberry.mutation
    async def create_group(self, input: GroupInput) -> GroupType:
        groups_collection = get_collection("groups")
        group_data = input.__dict__
        group_data["members"] = [member.__dict__ for member in input.members]
        result = await groups_collection.insert_one(group_data)
        group_data["_id"] = str(result.inserted_id)
        return GroupType(id=group_data["_id"],
                         group_name=group_data["group_name"],
                         members=[GroupMemberType(**member) for member in group_data["members"]],
                         trip_ids=group_data["trip_ids"])
    
    @strawberry.mutation
    async def update_group(self, id: str, input: GroupInput) -> Optional[GroupType]:
        groups_collection = get_collection("groups")
        group_data = input.__dict__
        group_data["members"] = [member.__dict__ for member in input.members]
        result = await groups_collection.update_one({"_id": ObjectId(id)}, {"$set": group_data})
        
        if result.matched_count:
            group_data["_id"] = id
            return GroupType(id=id,
                             group_name=group_data["group_name"],
                             members=[GroupMemberType(**member) for member in group_data["members"]],
                             trip_ids=group_data["trip_ids"])
        return None
    
    @strawberry.mutation
    async def delete_group(self, id: str) -> bool:
        groups_collection = get_collection("groups")
        result = await groups_collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0
