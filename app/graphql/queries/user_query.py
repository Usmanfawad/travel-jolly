from bson import ObjectId
import strawberry
from typing import Optional
from app.graphql.types.user_type import UserType
from app.db.session import get_collection

@strawberry.type
class UserQuery:
    @strawberry.field
    async def user(self, id: str) -> Optional[UserType]:
        users_collection = get_collection("user")
        user_data = await users_collection.find_one({"_id": ObjectId(id)})
        if user_data:
            return UserType(id=str(user_data["_id"]), email=user_data["email"])
        return None
    
schema = strawberry.Schema(query=UserQuery)