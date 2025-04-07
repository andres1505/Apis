from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
class DatabaseFutbol:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGO_URI"), tlsAllowInvalidCertificates=True) #Este es el string de conexión a la base de datos en el cluster de MongoDB y desactiva la validacion de ssl
        self.db = self.client[os.getenv("MONGO_DB_NAME")] #Este es el nombre de la base de datos
        
    def get_collection_futbolista(self): #nombre de la coleccion
        return self.db["COLLECTION_FUTBOLISTA"] #Coleccion env
    
    def get_collection_equipos(self): #nombre de la coleccion
        return self.db["COLLECTION_EQUIPOS"] #Coleccion env
    
    def get_collection_ligas(self): #nombre de la coleccion
        return self.db["COLLECTION_LIGAS"] #Coleccion env

database_futbol = DatabaseFutbol()
