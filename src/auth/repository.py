# zaprosi v basu dannyh || for example iz servisov hochesh vyszvat' parol' usera i otsuda ono propisano selectom usera

from src.auth.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class UserRepository:
    
    def __init__(self, db : AsyncSession):
        self.db = db


    async def get_user_by_mail(self, user_email : str) -> User | None:
        stmt = select(User).where(User.email == user_email)
        result = await self.db.execute(stmt)
        return result.scalars().first()
    

    async def create_user_db(self, **fields) -> User:
        user = User(**fields)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user



