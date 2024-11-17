from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.mysql import insert
from sqlalchemy import delete, select
from core.schemas.theme import ThemeCreate, ThemeUpdate

from core.models import Theme

from core.utils import logger


async def add_theme(session: AsyncSession, insert_theme: ThemeCreate) -> Theme:
    theme_dict = insert_theme.model_dump()
    theme_result = await session.scalars(insert(Theme).returning(Theme), [theme_dict])
    theme = theme_result.one()
    logger.info(f"theme_created = {theme} by user with id {insert_theme.user_id}")
    return theme


async def get_all_themes(
    session: AsyncSession,
) -> Sequence[Theme]:
    stmt = select(Theme)
    themes = await session.scalars(stmt)
    all_themes = themes.all()
    logger.info(f"list_all_themes = {all_themes}")
    return all_themes


async def get_theme_by_name(
    session: AsyncSession,
    name: str,
) -> Theme:
    stmt = select(Theme).where(Theme.name == name)
    theme_selected_by_name = await session.scalars(stmt)
    result = theme_selected_by_name.one()
    logger.info(f"theme_selected_by_name = {result}")
    return result


async def get_theme_by_user(
    session: AsyncSession,
    user_id: int,
) -> Theme:
    stmt = select(Theme).where(Theme.user_id == user_id)
    theme_selected_by_user = await session.scalars(stmt)
    result = theme_selected_by_user.all()
    logger.info(f"theme_selected_by_user = {result}")
    return result


async def update_theme(
    session: AsyncSession, theme: Theme, update_theme_values: ThemeUpdate
) -> None:
    update_theme_dict = update_theme_values.model_dump()
    insert_stmt = insert(Theme).values(
        id=theme.id, name=update_theme_dict["name"], user_id=theme.user_id
    )
    on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
        name=insert_stmt.inserted.name,
    )
    await session.execute(on_duplicate_key_stmt)
    logger.info(f"Theme with id: {theme.id} updated successfully")


async def delete_theme_by_id(
    session: AsyncSession,
    theme_id: int,
) -> str:
    stmt = delete(Theme).where(Theme.id == theme_id)
    await session.execute(stmt)
    logger.info(f"Theme with id: {theme_id} deleted successfully")
    await session.commit()
