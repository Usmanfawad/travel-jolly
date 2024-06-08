from datetime import date, datetime
from typing import Optional
import strawberry


@strawberry.type
class TripType:
    id: str
    name: str
    location: str
    description: str
    start_date: date
    end_date: date
    budget: Optional[float] = None
    user_id: str
    created_date: datetime


@strawberry.input
class TripInput:
    name: str
    location: str
    description: str
    start_date: date
    end_date: date
    budget: Optional[float] = None