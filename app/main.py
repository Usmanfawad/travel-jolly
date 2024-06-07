import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.api import router as api_router
from app.db.session import get_db


ORIGIN_LIST = ['*']


def get_application() -> FastAPI:
    ''' Configure, start and return the application '''

    application = FastAPI(
        title="Travel Platform",
        summary="Travel Platform panel",
        version="0.0.1"
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ORIGIN_LIST,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix="/api")
    get_db()
    return application


app = get_application()


@app.get("/")
def read_root():
    return "New Server is running"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get('PORT', 8000)))
