from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.rest.controllers.destination_controller import create_destination, get_destination_by_id, update_destination, delete_destination
from app.rest.schemas.destination import DestinationCreate, Destination
from app.dependencies.authDependencies.auth import JWTBearer
from app.db.session import get_db

router = APIRouter()

@router.post("/destinations", response_model=Destination)
async def create_new_destination(
    destination: DestinationCreate,
    current_user: str = Depends(JWTBearer()),
    db: AsyncIOMotorDatabase = Depends(get_db)
):
    return await create_destination(db, destination)

@router.get("/destinations/{id}", response_model=Destination)
async def read_destination(id: str, db: AsyncIOMotorDatabase = Depends(get_db), current_user: str = Depends(JWTBearer())):
    destination = await get_destination_by_id(db, id)
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    return destination

@router.put("/destinations/{id}", response_model=Destination)
async def update_existing_destination(
    id: str,
    destination_update: DestinationCreate,
    current_user: str = Depends(JWTBearer()),
    db: AsyncIOMotorDatabase = Depends(get_db)
):
    destination = await get_destination_by_id(db, id)
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    return await update_destination(db, id, destination_update)

@router.delete("/destinations/{id}", response_model=dict)
async def delete_existing_destination(
    id: str,
    current_user: str = Depends(JWTBearer()),
    db: AsyncIOMotorDatabase = Depends(get_db)
):
    destination = await get_destination_by_id(db, id)
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    return await delete_destination(db, id)
