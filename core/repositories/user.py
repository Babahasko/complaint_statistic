from sqlalchemy.ext.asyncio import AsyncSession, AsyncResult
from sqlalchemy import select, insert, delete, update, and_
from core.schemas.user import UserCreate

from core.models import User

from core.utils import logger


async def create_user(
    session: AsyncSession,
    insert_user: UserCreate,
) -> User:
    users_dict = [insert_user.model_dump()]
    logger.info(f"{users_dict}")
    user = await session.execute(insert(User), users_dict)
    return user


async def select_user_by_id(
    session: AsyncSession,
    user_id: int,
) -> User:
    stmt = select(User).where(User.id == user_id)
    user_selected_by_id = await session.scalars(stmt)
    return user_selected_by_id.first()


async def select_user_by_username(
    session: AsyncSession,
    username: str,
) -> User:
    stmt = select(User).where(User.username == username)
    user_selected_by_id = await session.scalars(stmt)
    return user_selected_by_id.all()[-1]


# async def create_user(
#     session: AsyncSession, insert_user: UserCreate
# ) -> ScalarResult[User]:
#     user_list = [insert_user.model_dump()]
#     user_result = await session.scalars(
#         insert(User).returning(User),
#         user_list,
#     )
#     result = user_result.all()
#     return result


#

#
# async def delete_complain(
#         session: AsyncSession,
#         id_to_delete: int
# ) -> None:
#     stmt = delete(User).where(and_(User.id == id_to_delete))
#     await session.execute(stmt)
#
# async def update_user_name(
#         session: AsyncSession,
#         id_to_update: int,
#         new_name: str
# ) -> None:
#     stmt = update(User).where(User.id == id_to_update).values(name=new_name)
#     await session.execute(stmt)
