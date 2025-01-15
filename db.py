from typing import Annotated
from fastapi import Depends
from sqlmodel import create_engine, text, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker

from .config import Config

engine = AsyncEngine(
    create_engine(
        url=Config.DATABASE_URL, 
        echo=True
    )
)

async def init_db():
    async with engine.begin() as conn:
        statement = text("SELECT NOW();")
        result = await conn.execute(statement)
        print(result.all())

        await conn.run_sync(SQLModel.metadata.create_all)    

async def get_session():
    Session = sessionmaker(
        bind=engine, 
        class_=AsyncSession, 
        expire_on_commit=False
    )

    async with Session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]