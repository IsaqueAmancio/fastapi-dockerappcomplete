from pydantic import validator, BaseModel, EmailStr
import re

class User(BaseModel):
    id: int
    username: str
    password: str
    user_email: EmailStr

@validator('username')
def validate_username(cls, value):
    if not re.match('^([a-z]|[A-Z]|[0-9]|-|_|@)+$', value):
        raise ValueError('Invalid username')
    return value