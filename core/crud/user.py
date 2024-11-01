from typing import Sequence

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.mysql import insert
from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload
from core.schemas import UserCreate, UserUpdate

from core.models import User

from core.utils import logger


async def add_user(
    session: AsyncSession,
    insert_user: UserCreate,
) -> User:
    user_dict = insert_user.model_dump()
    try:
        user_result = await session.scalars(insert(User).returning(User), [user_dict])
        user = user_result.one()
        logger.info(f"user_created = {user}")
        await session.commit()
        return user
    except Exception as e:
        await session.rollback()
        logger.info(f"Exception = {e.args}")
    finally:
        await session.close()


async def get_all_users(
    session: AsyncSession,
) -> Sequence[User]:
    stmt = select(User)
    all_users = await session.scalars(stmt)
    logger.info(f"list_all_users = {all_users}")
    return all_users.all()


async def get_user_by_id(
    session: AsyncSession,
    user_id: int,
) -> User:
    stmt = select(User).where(User.id == user_id)
    user_selected_by_id = await session.scalars(stmt)
    logger.info(f"user_selected_by_id = {user_selected_by_id.one}")
    return user_selected_by_id.one_or_none()


async def get_user_by_username(
    session: AsyncSession,
    username: str,
) -> User:
    stmt = select(User).where(User.username == username)
    user_selected_by_username = await session.scalars(stmt)
    result = user_selected_by_username.one_or_none()
    logger.info(f"user_selected_by_username = {result}")
    return result


async def get_user_by_telegramm_account_name(
    session: AsyncSession,
    telegramm_account: str,
) -> User:
    stmt = select(User).where(User.telegramm_account == telegramm_account)
    user_selected_by_telegramm_account = await session.scalars(stmt)
    result = user_selected_by_telegramm_account.one_or_none()
    logger.info(f"user_selected_by_telegramm_account = {result}")
    return result


async def get_user_themes(session: AsyncSession, user_id: int) -> User:
    stmt = select(User).options(selectinload(User.themes)).where(User.id == user_id)
    user = await session.scalars(stmt)
    result = user.one()
    logger.info(f"user_themes = {result.themes} for user with id {user_id}")
    return result.themes


async def get_user_surveillance(session: AsyncSession, user_id: int) -> User:
    stmt = (
        select(User).options(selectinload(User.surveillance)).where(User.id == user_id)
    )
    user = await session.scalars(stmt)
    result = user.one()
    logger.info(f"user_surveillance = {result.surveillance} for user with id {user_id}")
    return result.surveillance


async def get_user_complains(session: AsyncSession, user_id: int) -> User:
    stmt = select(User).options(selectinload(User.complains)).where(User.id == user_id)
    user = await session.scalars(stmt)
    result = user.one()
    logger.info(f"user_complains = {result.complains} for user with id {user_id}")
    return result.complains


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
    logger.info(f"User with id: {user.id} updated successfully")


async def delete_user_by_id(session: AsyncSession, user_id: int) -> None:
    try:
        stmt = delete(User).where(User.id == user_id)
        result = await session.execute(stmt)
        logger.info(f"rows to delete = {result.rowcount}")
        logger.info(f"User with id: {user_id} deleted successfully")
        await session.commit()
    except Exception as e:
        await session.rollback()
        logger.info(f"Exception = {e.args}")
        raise e
    finally:
        await session.close()
