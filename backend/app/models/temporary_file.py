# models/temporary_file.py
import uuid
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional

class TemporaryFile(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    filename: str
    file_path: str
    uploaded_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    expires_at: datetime  # TTL index in MongoDB should be created on this field
    download_limit: Optional[int] = None  # Optional limit on number of downloads
    current_download_count: int = Field(default=0)

    class Config:
        arbitrary_types_allowed = True
