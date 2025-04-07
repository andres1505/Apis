from pydantic import BaseModel


#se validan los datos de entrada y salida de la API utilizando pydantic
#modelo base pelicula
class PeliculaBase(BaseModel):
    id: int
    title: str
    year: int
    category: str