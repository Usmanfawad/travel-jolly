import os
import time
from dotenv import load_dotenv
from fastapi import Header, HTTPException
import jwt
from app.controllers.user_controller import get_user_by_id

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

def auth_deps(authorization: str = Header(None)):
    token = None
    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ")[1]
    if not token:
        raise HTTPException(status_code=401, detail="Token is missing")

    try:
        print("Token:", token, "Secret Key:", SECRET_KEY)
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print("Decoded Token:", decoded_token)

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
