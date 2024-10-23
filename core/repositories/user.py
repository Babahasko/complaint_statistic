from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.mysql import insert
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from core.schemas import UserCreate, UserUpdate

from core.models import User

from core.utils import logger


async def add_user(
    session: AsyncSession,
    insert_user: UserCreate,
) -> User:
    user_dict = insert_user.model_dump()
    logger.info(f"{user_dict}")
    user_result = await session.scalars(insert(User).returning(User), [user_dict])
    user = user_result.one()
    logger.info(f"user created {user}")
    return user


async def get_all_users(
    session: AsyncSession,
) -> Sequence[User]:
    stmt = select(User)
    list_all_users = await session.scalars(stmt)
    return list_all_users.all()


async def get_user_by_id(
    session: AsyncSession,
    user_id: int,
) -> User:
    stmt = select(User).where(User.id == user_id)
    user_selected_by_id = await session.scalars(stmt)
    return user_selected_by_id.one_or_none()


async def get_user_by_username(
    session: AsyncSession,
    username: str,
) -> User:
    stmt = select(User).where(User.username == username)
    user_selected_by_id = await session.scalars(stmt)
    return user_selected_by_id.first()


async def select_user_with_themes(session: AsyncSession, user_id: int) -> User:
    stmt = select(User).options(selectinload(User.themes)).where(User.id == user_id)
    user = await session.scalars(stmt)
    return user.one()


async def select_user_with_surveillance(session: AsyncSession, user_id: int) -> User:
    stmt = (
        select(User).options(selectinload(User.surveillance)).where(User.id == user_id)
    )
    user = await session.scalars(stmt)
    return user.one()


async def select_user_with_complains(session: AsyncSession, user_id: int) -> User:
    stmt = select(User).options(selectinload(User.complains)).where(User.id == user_id)
    user = await session.scalars(stmt)
    return user.one()


async def update_user_by_id(
    session: AsyncSession, user: User, update_user_values: UserUpdate
) -> None:
    update_user_dict = update_user_values.model_dump()
    insert_stmt = insert(User).values(
        id=user.id,
        telegramm_account=user.telegramm_account,
        username=update_user_dict["username"],
    )
    on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
        username=insert_stmt.inserted.username,
    )
    await session.execute(on_duplicate_key_stmt)
