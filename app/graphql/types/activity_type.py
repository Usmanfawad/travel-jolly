import strawberry
from typing import List, Optional

from app.graphql.types.destination_type import SuggestionInput, SuggestionType


@strawberry.type
class ActivityType:
    id: str
    destination_id: str
    name: str
    description: str
    suggestions: Optional[List[SuggestionType]] = None

@strawberry.input
class ActivityInput:
    destination_id: str
    name: str
    description: str
    suggestions: Optional[List[SuggestionInput]] = None