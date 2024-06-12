import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_PW: str = os.getenv("MONGODB_PASSWORD")
CONN_STRING: str = (
    f"mongodb+srv://zahidfaakhir:{MONGODB_PW}@cluster0.ojvotpr.mongodb.net/?retryWrites=true&w=majority"
)
SECRET_KEY: str = os.environ.get("SECRET_KEY")
JWT_SECRET: str = os.getenv("JWT_SECRET")
JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")
