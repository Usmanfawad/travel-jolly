import os
import time
from bson import ObjectId
from dotenv import load_dotenv
from fastapi import Header, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from app.rest.controllers.user_controller import get_user_by_id
from app.db.session import get_db

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")


ROLE_PROTECTED_ROUTES = ['/groups']

REQUIRED_PERISSIONS = {
    "GET": ["read"],
    "PUT": ["update"],
    "DELETE": ["delete"]
}

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            user_id = self.auth_deps(credentials.credentials)
            if any(route in request.url.path for route in ROLE_PROTECTED_ROUTES):
                await self.role_deps(user_id, request)
            return user_id
        
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def auth_deps(self, token: str):
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

            if "exp" not in decoded_token or not isinstance(decoded_token["exp"], int):
                raise ValueError("Expiration Time claim (exp) must be an integer.")

            if decoded_token["exp"] < time.time():
                raise jwt.ExpiredSignatureError

            current_user = get_user_by_id(decoded_token["user_id"])
            if not current_user:
                raise HTTPException(status_code=404, detail="User not found")

            return decoded_token["user_id"]

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
        except Exception as e:
            print("Exception at auth middleware:", e)
            raise HTTPException(status_code=500, detail="Server Error")

    async def role_deps(self, user_id, req:Request):
        if req.method in ["GET", "PUT", "DELETE"]:
            group_id = req.url.path.split("/")[-1]
            db = get_db()
            group_collection = db.get_collection("groups")
            group_data = await group_collection.find_one({"_id": ObjectId(group_id)})
            if group_data is None:
                raise HTTPException(status_code=404, detail="Group not found")
            if group_data['members']:
                if user_id not in [member['user_id'] for member in group_data['members']]:
                    raise HTTPException(status_code=403, detail="You are not a member of this group")
                roles_col = db.get_collection("roles")
                for member in group_data['members']:
                    if member['user_id'] == user_id:
                        user_role = await roles_col.find_one({"_id": ObjectId(member['role_id'])})
                        if not user_role:
                            raise HTTPException(status_code=403, detail="You do not have the required role to perform this action")
                        if all([perm not in REQUIRED_PERISSIONS[req.method] for perm in user_role['permissions']]):
                            raise HTTPException(status_code=403, detail="You do not have the required role to perform this action")
                        break
            else:
                raise HTTPException(status_code=403, detail="You are not a member of this group")
