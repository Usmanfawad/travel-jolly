import os
import time
import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from passlib.context import CryptContext
from app.db.session import get_db
from app.rest.schemas.user import UserCreate

SECRET_KEY = os.environ.get("JWT_SECRET")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def login(data: UserCreate):
    email = data.email.lower()
    password = data.password

    try:
        db = get_db()
        user_collection = db.get_collection("user")
        user_data = await user_collection.find_one({"email": email})
        if user_data is None:
            raise HTTPException(status_code=404, detail="User not found")

        user_id = user_data["_id"]
        hashed_password = user_data["password"]

        if pwd_context.verify(password, hashed_password):
            expiration_time = int(time.time()) + 43200 # 12 hours
            payload = {"email": email, "user_id": str(user_id), "exp": expiration_time}
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
            return {"status": 200, "message": "Login successful", "token": token}
        else:
            raise HTTPException(status_code=401, detail="Invalid password")

    except Exception as e:
        raise HTTPException(status_code=500, detail="Server Error: " + str(e))
