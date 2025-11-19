# API router



from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.db import get_db 



router = APIRouter()


@router.get("/check")
async def check(db: AsyncSession=Depends(get_db)):
    res = await db.execute(text("SELECT 1"))
    return res.scalar()
