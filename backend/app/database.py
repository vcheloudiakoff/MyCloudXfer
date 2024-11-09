from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
import asyncio

# Charger les variables depuis le fichier .env
load_dotenv()

# Charger l'URL de la base de données à partir des variables d'environnement
DATABASE_URL = os.getenv("DATABASE_URL")

# Créer le moteur de base de données asynchrone
engine = create_async_engine(DATABASE_URL, echo=True)

# Créer une session asynchrone pour interagir avec la base de données
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

Base = declarative_base()

# Fonction pour obtenir une session de base de données
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Appeler init_db lorsque ce fichier est exécuté directement
if __name__ == "__main__":
    asyncio.run(init_db())