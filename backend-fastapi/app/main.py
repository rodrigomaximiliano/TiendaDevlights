from fastapi import FastAPI
from app.auth import router as auth_router
from app.product import router as product_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto por la URL de tu frontend en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(product_router, prefix="/store")
