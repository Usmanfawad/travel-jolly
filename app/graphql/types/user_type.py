import strawberry

@strawberry.type
class UserType:
    id: str
    email: str

@strawberry.input
class UserInput:
    email: str
    password: str
