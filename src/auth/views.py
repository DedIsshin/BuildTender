# API router

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from src.database.db import get_db 
from src.auth.services import UserServices
from src.auth.schemas import UserCreate, UserRead, UserLogin, AuthToken
from src.auth.dependencies import get_current_user



router = APIRouter(
    tags=["auth"]
)


@router.post("/register", response_model=UserRead)
async def register_user(user_data: UserCreate, db: AsyncSession=Depends(get_db)):
    services = UserServices(db)
    return await services.register(user_data)



@router.post("/login", response_model=AuthToken)
async def login_user(user_data: UserLogin, db: AsyncSession=Depends(get_db)):
    services = UserServices(db)
    return await services.login(user_data)


@router.get("/me")
async def get_me(current_user = Depends(get_current_user)):
    return current_user


