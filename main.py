from fastapi import FastAPI
from routes.pelicula_routes import router as pelicula_router
from routes import futbol_routes


app = FastAPI()
#Router de peliculas
app.include_router(pelicula_router, prefix="/peliculas", tags=["peliculas"])

#Router de futbol
app.include_router(futbol_routes.router, prefix="/futbol", tags=["Futbol"])

#Endpoint default
@app.get("/")
async def root():
    return {"message": "Hello Wordl"}
