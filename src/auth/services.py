#buisness logic - proverka parolei, est' li user, vse metody po logike

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException


from src.auth.repository import UserRepository
from src.auth.schemas import UserCreate
from src.utils.security import get_password_hash, verify_password

class UserServices:

    def __init__(self, db : AsyncSession):
        self.repository = UserRepository(db)



    async def register(self, user_to_create : UserCreate):
        existing = await self.repository.get_user_by_mail(user_to_create.email)
        if existing:
            raise HTTPException(status_code=400, detail="Email already exists")
        hashed_pass = get_password_hash(user_to_create.password)

        return await self.repository.create_user_db(
            email=user_to_create.email,
            password_hash=hashed_pass,
            phone=user_to_create.phone,
            full_name=user_to_create.full_name,
            role=user_to_create.role,
            is_active=user_to_create.is_active,
        )

