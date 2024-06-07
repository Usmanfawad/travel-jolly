from typing import Optional
from bson import ObjectId
import strawberry
from app.db.session import get_collection
from app.graphql.types.user_type import UserType, UserInput
from app.rest.controllers.user_controller import hash_password

@strawberry.type
class UserMutation:
    @strawberry.mutation
    async def create_user(self, input: UserInput) -> UserType:
        users_collection = get_collection("user")
        user_data = input.__dict__
        user_data["password"] = hash_password(user_data["password"])
        result = await users_collection.insert_one(user_data)
        user_data["_id"] = str(result.inserted_id)
        return UserType(id=user_data["_id"], email=user_data["email"])
    
    @strawberry.mutation
    async def update_user(self, id: str, input: UserInput) -> Optional[UserType]:
        users_collection = get_collection("user")
        user_data = input.__dict__
        if user_data.get("password"):
            user_data["password"] = hash_password(user_data["password"])
            
        result = await users_collection.update_one({"_id": ObjectId(id)}, {"$set": user_data})
        
        if result.matched_count:
            user_data["_id"] = id
            return UserType(id=id, email=user_data["email"])
        return None
    
    @strawberry.mutation
    async def delete_user(self, id: str) -> bool:
        users_collection = get_collection("user")
        result = await users_collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0
