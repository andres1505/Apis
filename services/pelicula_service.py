from fastapi import HTTPException
from db.database_pelicula import database_pelicula
from bson import ObjectId
from models.pelicula_models import PeliculaBase

# Esta funcion devuelve la lista de peliculas de la base de datos
def get_peliculas():
    collection = database_pelicula.get_collection("Peliculas")
    peliculas = list(collection.find({}, {"_id": 0})) #excluye el campo _id de la consulta
    if not peliculas:
        raise HTTPException(status_code=404, detail="No se encontraron peliculas, agrega alguna") #Manejador de excepciones para el caso en que no se encuentren peliculas
    return peliculas


#esta funcion devuelve una pelicula de la base de datos por su id
def get_pelicula_by_id(pelicula_id: int):
    collection = database_pelicula.get_collection("Peliculas")
    pelicula = collection.find_one({"id": pelicula_id}, {"_id": 0})
    if not pelicula:
        raise HTTPException(status_code=404, detail="Pelicula no encontrada, prueba con otro id") #Manejador de excepciones para el caso en que no se encuentre la pelicula
    return pelicula


#Esta funcion permite agregar una pelicula a la base de datos
def add_pelicula(pelicula: PeliculaBase):
    collection = database_pelicula.get_collection("Peliculas")
    if collection.find_one({"id": pelicula.id}): #Verifica si la pelicula ya existe en la base de datos
        raise HTTPException(status_code=400, detail="La pelicula ya existe, cambia el id") #Manejador de excepciones para el caso en que la pelicula ya exista
    pelicula_dict = pelicula.dict()#Se convierte el objeto pelicula a un diccionario    
    collection.insert_one(pelicula_dict) #Se inserta la pelicula en la base de datos
    return{"Mensaje": "Pelicula insertada :D"}


#Esta funcion permite actualizar una pelicula en la base de datos
def update_pelicula(pelicula_id: int, pelicula: PeliculaBase):
    collection = database_pelicula.get_collection("Peliculas")
    pelicula_dict = pelicula.dict()# Vuelve a convertir el objeto pelicula a un diccionario
    # Eliminar 'id' para evitar conflictos al actualizar
    if "id" in pelicula_dict:
        del pelicula_dict["id"] # Eliminar el campo id del diccionario para que no se actualice porque no es necesario
    resultado = collection.update_one({"id": pelicula_id}, {"$set": pelicula_dict})
    if resultado.matched_count == 0: #Verifica si la pelicula existe
        raise HTTPException(status_code=404, detail="Pelicula no encontrada, verifica el id") #Manejador de excepciones para el caso en que la pelicula no exista    
    return{"Mensaje": "Pelicula actualizada :D"}


#Esta funcion permite eliminar una pelicula de la base de datos
def eliminar_pelicula(pelicula_id: int):
    collection = database_pelicula.get_collection("Peliculas")
    resultado = collection.delete_one({"id": pelicula_id})
    if resultado.deleted_count == 0: #Verifica si la pelicula existe
        raise HTTPException(status_code=404, detail="Pelicula no encontrada, verifica el id") #Manejador de excepciones para el caso en que la pelicula no exista
    return{"Mensaje": "Pelicula eliminada :("}