from fastapi import APIRouter
from app.database import db
from app.schemas import ProductSchema
from bson import ObjectId

router = APIRouter()

def product_serializer(product) -> dict:
    return {
        "id": str(product["_id"]),  # Convertimos el ObjectId a string
        "name": product["name"],
        "price": product["price"],
        # Agrega los demás campos de tu producto aquí
    }

@router.post("/product")
async def create_product(product: ProductSchema):
    product = product.dict()
    await db["products"].insert_one(product)
    return {"msg": "Product created successfully"}

@router.get("/products")
async def list_products():
    products = await db["products"].find().to_list(100)
    return [product_serializer(product) for product in products]
