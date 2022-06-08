from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    address_id: int


class User(UserBase):
    address: dict
    id: int
    is_active: bool

    class Config:
        orm_mode = True
