import strawberry

@strawberry.type
class UserType:
    id: str
    email: str

@strawberry.type
class UserInput:
    email: str
    password: str
