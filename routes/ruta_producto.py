from fastapi import APIRouter
from services.servicio_producto import obtener_productos

router = APIRouter()

# para verlo en el postman
@router.get("/productos")
async def obtener_productos_api():
    productos = obtener_productos()
    return productos
