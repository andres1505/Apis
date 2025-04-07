from pydantic import BaseModel
from typing import Optional, List

#se validan los datos de entrada y salida de la API utilizando pydantic
class PeliculaBase(BaseModel):
    id: int
    title: str
    year: int
    category: str