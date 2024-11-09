# Utiliser une image Python optimisée pour FastAPI
FROM python:3.12-slim

# Définir le dossier de travail
WORKDIR /app

# Copier le fichier de dépendances avant d’ajouter le reste du code pour tirer parti du cache Docker
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier les fichiers du backend
COPY . /app

# Exposer le port pour FastAPI
EXPOSE 8001

# Démarrer le serveur FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
