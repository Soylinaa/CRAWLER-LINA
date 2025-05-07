from fastapi import FastAPI
from routes.ruta_producto import router

app = FastAPI()
# Incluye la ruta de productos
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de productos de Maquillaje"}



