from sqlalchemy.ext.asyncio import AsyncSession, AsyncResult
from sqlalchemy import select, insert, delete, update, and_
from core.schemas.theme import ThemeCreate

from core.models import Theme

from core.utils import logger


async def create_theme(session: AsyncSession, insert_theme: ThemeCreate) -> Theme:
    theme_dict = insert_theme.model_dump()
    theme_result = await session.scalars(insert(Theme).returning(Theme), [theme_dict])
    theme = theme_result.one()
    logger.info(f"theme created {theme}")
    return theme
