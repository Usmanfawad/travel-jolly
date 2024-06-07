import strawberry
from typing import List, Optional

from app.graphql.types.destination_type import SuggestionType


@strawberry.type
class ActivityType:
    id: str
    destination_id: str
    name: str
    description: str
    suggestions: Optional[List[SuggestionType]] = None

@strawberry.type
class ActivityInput:
    destination_id: str
    name: str
    description: str
    suggestions: Optional[List[SuggestionType]] = None