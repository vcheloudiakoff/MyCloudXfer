# routers/files.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.permanent_file import PermanentFile
from app.schemas import PermanentFileCreate, PermanentFileOut
from sqlalchemy.future import select

router = APIRouter()

@router.post("/permanent-files/", response_model=PermanentFileOut)
async def create_permanent_file(file: PermanentFileCreate, db: AsyncSession = Depends(get_db)):
    new_file = PermanentFile(**file.model_dump())
    db.add(new_file)
    await db.commit()
    await db.refresh(new_file)
    return new_file

@router.get("/permanent-files/{file_id}", response_model=PermanentFileOut)
async def read_permanent_file(file_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PermanentFile).where(PermanentFile.id == file_id))
    file = result.scalar_one_or_none()
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return file
