from bson import ObjectId
from passlib.context import CryptContext
from fastapi import HTTPException
from app.schemas.user import UserCreate, UserUpdate, User

from app.db.session import get_db
db = get_db()
user_collection = db.get_collection("user")

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Helper Functions
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# CRUD Operations
async def get_user_by_id(user_id: str) -> User:
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
        del user["password"]
        return user
        
    else:
        raise HTTPException(status_code=404, detail="User not found")

async def create_user(user: UserCreate) -> User:
    hashed_password = hash_password(user.password)
    user_dict = user.model_dump()
    user_dict["password"] = hashed_password
    user = await user_collection.find_one({"email": user.email})
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
        
    result = await user_collection.insert_one(user_dict)
    new_user = await get_user_by_id(str(result.inserted_id))
    return new_user

async def update_user(user_id: str, user_update: UserUpdate) -> User:

    if user_update.password:
        user_update.password = hash_password(user_update.password)
        
    await user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user_update.model_dump(exclude_unset=True)}
    )
    updated_user = await get_user_by_id(user_id)
    del updated_user["password"]
    return updated_user

async def delete_user(user_id: str):
    result = await user_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
