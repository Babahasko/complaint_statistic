from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.mysql import insert
from sqlalchemy import delete
from core.schemas.theme import ThemeCreate, ThemeUpdate

from core.models import Theme, User

from core.utils import logger


async def add_theme(session: AsyncSession, insert_theme: ThemeCreate) -> Theme:
    theme_dict = insert_theme.model_dump()
    theme_result = await session.scalars(insert(Theme).returning(Theme), [theme_dict])
    theme = theme_result.one()
    logger.info(f"theme_created = {theme} by user with id {insert_theme.user_id}")
    return theme


async def update_theme_by_user(
    session: AsyncSession, theme: Theme, user: User, update_theme_values: ThemeUpdate
) -> None:
    update_theme_dict = update_theme_values.model_dump()
    insert_stmt = insert(Theme).values(
        id=theme.id, name=update_theme_dict["name"], user_id=user.id
    )
    on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
        name=insert_stmt.inserted.name,
    )
    await session.execute(on_duplicate_key_stmt)


async def delete_theme_by_id(
    session: AsyncSession,
    theme_id: int,
) -> str:
    stmt = delete(Theme).where(Theme.id == theme_id)
    await session.execute(stmt)
