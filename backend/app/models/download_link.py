# models/download_link.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import uuid

class DownloadLink(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    file_id: str  # Référence vers un fichier dans TemporaryFile ou PermanentFile
    expires_at: datetime
    password_hash: Optional[str] = None  # Stockage du hash du mot de passe (si nécessaire)
    download_count: int = Field(default=0)
    max_downloads: Optional[int] = None  # Limite de téléchargement si définie
