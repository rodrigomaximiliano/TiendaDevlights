from fastapi import FastAPI
from app.auth import router as auth_router
from app.product import router as product_router
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

# Carga la URI desde el archivo .env
MONGODB_URI = os.getenv("MONGODB_URI")

# Inicializa el cliente de MongoDB
client = AsyncIOMotorClient(MONGODB_URI)
db = client["my_store_db"]

app = FastAPI()

# Configuración de CORS para permitir solicitudes desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluye las rutas de autenticación y productos
app.include_router(auth_router, prefix="/auth")
app.include_router(product_router, prefix="/store")
