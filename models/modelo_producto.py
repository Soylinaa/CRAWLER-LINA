from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    titulo: str
    foto: str
    precio: str
    color: Optional[str] = None  # El color es opcional
