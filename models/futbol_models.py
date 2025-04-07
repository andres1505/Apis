from pydantic import BaseModel

#Modelo base Equipo
class Equipo(BaseModel):
    id: int
    nombre: str
    pais: str

#Modelo base Jugador
class Jugador(BaseModel):
    id: int
    nombre: str
    posicion: str
    equipo_id: str
    
#Modelo base Evento
class Liga(BaseModel):
    id: int
    nombre: str
    abreviatura: str
    imagen: str
