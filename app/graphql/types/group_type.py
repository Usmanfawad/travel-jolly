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

@strawberry.input
class GroupMemberInput:
    user_id: str
    role_id: str

@strawberry.input
class GroupInput:
    group_name: str
    members: List[GroupMemberInput]
    trip_ids: List[str]