from fastapi import FastAPI
from routes.pelicula_routes import router as pelicula_router

app = FastAPI()
app.include_router(pelicula_router, prefix="/peliculas", tags=["peliculas"])

@app.get("/")
async def root():
    return {"message": "Hello World"}
