from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True