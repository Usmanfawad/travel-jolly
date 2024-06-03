from fastapi import APIRouter, Depends, HTTPException
from app.controllers.trip_controller import get_trip_by_id, create_trip, update_trip, delete_trip
from app.schemas.trip import TripCreate, TripUpdate, Trip
from app.dependencies.authDependencies.auth import auth_deps
from app.db.session import get_db

router = APIRouter()

@router.get("/trips/{id}", response_model=Trip)
async def read_trip(id: str, db= Depends(get_db)):
    return await get_trip_by_id(db, id)

@router.post("/trips", response_model=Trip)
async def create_new_trip(trip: TripCreate, current_user: str = Depends(auth_deps), db= Depends(get_db)):
    return await create_trip(db, trip, current_user)

@router.put("/trips/{id}", response_model=Trip)
async def update_existing_trip(id: str, trip_update: TripUpdate, current_user: str = Depends(auth_deps), db= Depends(get_db)):
    trip = await get_trip_by_id(db, id)
    if trip["user_id"] != current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await update_trip(db, id, trip_update)

@router.delete("/trips/{id}", response_model=dict)
async def delete_existing_trip(id: str, current_user: str = Depends(auth_deps), db= Depends(get_db)):
    trip = await get_trip_by_id(db, id)
    if trip["user_id"] != current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await delete_trip(db, id)
