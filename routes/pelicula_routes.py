from fastapi import APIRouter
from models.pelicula_models import PeliculaBase
from services.pelicula_service import get_peliculas, get_pelicula_by_id, add_pelicula, update_pelicula, eliminar_pelicula

router = APIRouter()

@router.get("/prueba")  #ruta de prueba
async def read_root():   #funcion de prueba
    return {"message": "Hello peliculas"}
    
#lista general de peliculas
@router.get("/lista", response_model=list)
async def get_peliculas_list():
    peliculas = get_peliculas()
    return peliculas

#lista de peliculas por id
@router.get("/{pelicula_id}", response_model=PeliculaBase)
async def get_pelicula(pelicula_id: int):
    pelicula = get_pelicula_by_id(pelicula_id)
    if pelicula:
        return pelicula
    

#agregar una pelicula a la base de datos
@router.post("/agregar", response_model=dict)
async def create_pelicula(pelicula: PeliculaBase):
    return add_pelicula(pelicula)

#Actualizar una pelicula en la base de datos
@router.put("/actualizar/{pelicula_id}", response_model=dict)
async def actualizar_pelicula(pelicula_id: int, pelicula: PeliculaBase):
    return update_pelicula(pelicula_id, pelicula)

#Eliminar una pelicula de la base de datos
@router.delete("/eliminar/{pelicula_id}", response_model=dict)
async def delete_pelicula(pelicula_id: int):
    return eliminar_pelicula(pelicula_id)