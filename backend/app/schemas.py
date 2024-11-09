# schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TemporaryFileCreate(BaseModel):
    filename: str
    file_path: str
    expires_at: datetime
    download_limit: Optional[int] = None

class TemporaryFileOut(BaseModel):
    id: str
    filename: str
    uploaded_at: datetime
    expires_at: datetime
    download_limit: Optional[int]
    current_download_count: int

class PermanentFileCreate(BaseModel):
    filename: str
    file_path: str
    folder_id: Optional[int] = None

class PermanentFileOut(BaseModel):
    id: int
    filename: str
    uploaded_at: datetime
    folder_id: Optional[int]
