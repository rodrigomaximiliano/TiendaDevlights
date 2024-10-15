from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    password: str

class ProductSchema(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
