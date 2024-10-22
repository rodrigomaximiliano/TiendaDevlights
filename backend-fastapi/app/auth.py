from fastapi import APIRouter, HTTPException
from app.database import db
from app.schemas import UserSchema
import bcrypt

router = APIRouter()

@router.post("/register")
async def register(user: UserSchema):
    # Hash de la contraseña usando bcrypt
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    user_data = {"username": user.username, "password": hashed_password}
    
    # Inserción del usuario en la base de datos
    await db["users"].insert_one(user_data)
    return {"msg": "User registered successfully"}

@router.post("/login")
async def login(user: UserSchema):
    # Busca el usuario en la base de datos
    db_user = await db["users"].find_one({"username": user.username})
    
    # Verifica que el usuario exista y que la contraseña coincida
    if not db_user or not bcrypt.checkpw(user.password.encode('utf-8'), db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return {"msg": "Logged in successfully"}
