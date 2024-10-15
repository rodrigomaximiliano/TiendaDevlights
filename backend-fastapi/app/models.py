from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    username: str
    password: str

class Product(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
