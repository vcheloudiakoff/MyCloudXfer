import motor.motor_asyncio
import os

# Charger l'URL de MongoDB à partir des variables d'environnement
MONGODB_URL = os.getenv("MONGODB_URL")

# Créer un client MongoDB asynchrone
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.mycloudxfer  # Nom de la base de données MongoDB
