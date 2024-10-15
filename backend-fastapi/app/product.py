from fastapi import APIRouter
from app.database import db
from app.schemas import ProductSchema

router = APIRouter()

@router.post("/product")
async def create_product(product: ProductSchema):
    await db["products"].insert_one(product.dict())
    return {"msg": "Product created successfully"}

@router.get("/products")
async def list_products():
    products = await db["products"].find().to_list(100)
    return products
