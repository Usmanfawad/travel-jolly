from fastapi import APIRouter, Depends, HTTPException
from app.controllers.activity_controller import get_activity_by_id, create_activity, update_activity, delete_activity
from app.schemas.activity import ActivityCreate, ActivityUpdate, Activity
from app.dependencies.authDependencies.auth import JWTBearer
from app.db.session import get_db

router = APIRouter()

@router.get("/activities/{id}", response_model=Activity)
async def read_activity(id: str, db= Depends(get_db), current_user: str = Depends(JWTBearer())):
    return await get_activity_by_id(db, id)

@router.post("/activities", response_model=Activity)
async def create_new_activity(activity: ActivityCreate, current_user: str = Depends(JWTBearer()), db= Depends(get_db)):
    return await create_activity(db, activity)

@router.put("/activities/{id}", response_model=Activity)
async def update_existing_activity(id: str, activity_update: ActivityUpdate, current_user: str = Depends(JWTBearer()), db= Depends(get_db)):
    activity = await get_activity_by_id(db, id)
    return await update_activity(db, id, activity_update)

@router.delete("/activities/{id}", response_model=dict)
async def delete_existing_activity(id: str, current_user: str = Depends(JWTBearer()), db= Depends(get_db)):
    return await delete_activity(db, id)
