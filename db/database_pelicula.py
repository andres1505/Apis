from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class DatabasePelicula:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGO_URI"), tlsAllowInvalidCertificates=True) #Este es el string de conexión a la base de datos en el cluster de MongoDB y desactiva la validacion de ssl
        self.db = self.client[os.getenv("MONGO_COLLECTION")] #Este es el nombre de la base de datos en el cluster de MongoDB
        
    def get_collection(self, Peliculas):
        return self.db[Peliculas]

database_pelicula = DatabasePelicula()