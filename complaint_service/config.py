from typing import AsyncGenerator
from dotenv import load_dotenv
import os

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()

class DatabaseConfig:
    def __init__(
            self,
            url: str,
            echo: bool = False,
            echo_pool: bool = False,
            pool_size: int = 5,
            max_overflow: int = 10,
    ) -> None:
        self.url = url
        self.engine: AsyncEngine = create_async_engine(
            url = url,
            echo = echo,
            echo_pool = echo_pool,
            pool_size = pool_size,
            max_overflow = max_overflow,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind = self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session

class Settings:
    def __init__(self):
        self.db = DatabaseConfig(url=str(os.getenv('MARIADB_URL')))

settings = Settings()