from fastapi import APIRouter
from services.ligas_service import obtener_ligas
from services.equipos_service import obtener_equipos
from services.jugadores_service import obtener_jugadores

router = APIRouter()

@router.get("/ligas")
def get_ligas():
    return obtener_ligas()

@router.get("/equipos")
def get_equipos():
    return obtener_equipos()

@router.get("/jugadores")
def get_jugadores():
    return obtener_jugadores()
