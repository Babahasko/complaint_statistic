from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession, AsyncResult
from sqlalchemy import select, insert, delete, update, and_
from sqlalchemy.orm import joinedload, selectinload
from core.schemas.user import UserCreate

from core.models import User

from core.utils import logger


async def create_user(
    session: AsyncSession,
    insert_user: UserCreate,
) -> User:
    user_dict = insert_user.model_dump()
    logger.info(f"{user_dict}")
    user_result = await session.scalars(insert(User).returning(User), [user_dict])
    user = user_result.one()
    logger.info(f"user created {user}")
    return user


async def select_all_users(
    session: AsyncSession,
) -> Sequence[User]:
    stmt = select(User)
    list_all_users = await session.scalars(stmt)
    return list_all_users.all()


async def select_user_by_id(
    session: AsyncSession,
    user_id: int,
) -> User:
    stmt = select(User).where(User.id == user_id)
    user_selected_by_id = await session.scalars(stmt)
    return user_selected_by_id.one_or_none()


async def select_user_by_username(
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
