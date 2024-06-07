import strawberry
from typing import List, Optional

@strawberry.type
class GroupMemberType:
    user_id: str
    role_id: str

@strawberry.type
class GroupType:
    id: str
    group_name: str
    members: List[GroupMemberType]
    trip_ids: List[str]

@strawberry.type
class GroupInput:
    group_name: str
    members: List[GroupMemberType]
    trip_ids: List[str]