# API router



from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from src.database.db import get_db 
from src.auth.services import UserServices
from src.auth.schemas import UserCreate, UserRead






router = APIRouter()


@router.post("/register", response_model=UserRead)
async def register_user(user_data: UserCreate, db: AsyncSession=Depends(get_db)):
    services = UserServices(db)
    return await services.register(user_data)
