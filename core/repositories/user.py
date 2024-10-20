from sqlalchemy.ext.asyncio import AsyncSession, AsyncResult
from sqlalchemy import select, insert, delete, update, and_
from core.schemas.user import UserCreate

from core.models import User

from core.utils import logger


async def create_user(
    session: AsyncSession,
    insert_user: UserCreate,
) -> User:
    users_list = [insert_user.model_dump()]
    result = await session.execute(insert(User), users_list)
    return result


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
# async def select_user(
#         session: AsyncSession,
#         select_user_id: int,
# ) -> ScalarResult[User]:
#     stmt = select(User).where(User.id == select_user_id)
#     user_selected_by_id = await session.scalars(stmt)
#     return user_selected_by_id.all()
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
