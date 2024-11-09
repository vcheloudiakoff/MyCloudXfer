# crud/temporary_file.py
from typing import Optional
from mongodb import db
from models.temporary_file import TemporaryFile
from datetime import datetime, timezone

async def create_temporary_file(data: dict) -> TemporaryFile:
    file_data = {**data, "uploaded_at": datetime.now(timezone.utc)}
    result = await db.temporary_files.insert_one(file_data)
    file_data["_id"] = str(result.inserted_id)
    return TemporaryFile(**file_data)

async def get_temporary_file(file_id: str) -> Optional[TemporaryFile]:
    file_data = await db.temporary_files.find_one({"_id": file_id})
    return TemporaryFile(**file_data) if file_data else None
