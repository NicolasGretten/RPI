from pydantic import BaseModel


class AddressBase(BaseModel):
    city: str
    zip_code: str
    adress_line_1: str


class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True
