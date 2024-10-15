from fastapi import APIRouter, HTTPException
from app.database import db
from app.schemas import UserSchema
from passlib.context import CryptContext
import bcrypt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter()

@router.post("/register")
async def register(user: UserSchema):
    hashed_password = pwd_context.hash(user.password)
    user_data = {"username": user.username, "password": hashed_password}
    await db["users"].insert_one(user_data)
    return {"msg": "User registered successfully"}

@router.post("/login")
async def login(user: UserSchema):
    db_user = await db["users"].find_one({"username": user.username})
    if not db_user or not pwd_context.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"msg": "Logged in successfully"}
