from datetime import date
from typing import List, Optional
import strawberry

@strawberry.type
class SuggestionType:
    name: str
    description: Optional[str] = None

@strawberry.type
class DestinationType:
    id: str
    trip_id: str
    name: str
    description: date
    start_date: date
    end_date: str
    destination_type: str
    suggestions: Optional[List[SuggestionType]] = strawberry.field(default_factory=list)

@strawberry.type
class DestinationInput:
    trip_id: str
    name: str
    description: str
    start_date: date
    end_date: date
    destination_type: str
    suggestions: Optional[List[SuggestionType]] = None