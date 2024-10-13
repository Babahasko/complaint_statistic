from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert,delete, and_, ScalarResult
from core.schemas.user import UserCreate
from core.models.base import User


async def create_user(
        session: AsyncSession,
        insert_user: UserCreate
) -> ScalarResult[User]:
    user_list = [insert_user.model_dump()]
    user_result = await session.scalars(
        insert(User).returning(User), user_list,
    )
    result = user_result.all()
    return result

async def select_user(
        session: AsyncSession,
        select_user_id: int,
) -> ScalarResult[User]:
    stmt = select(User).where(User.id == select_user_id)
    user_selected_by_id = await session.scalars(stmt)
    return user_selected_by_id.all()

async def delete_complain(
        session: AsyncSession,
        id_to_delete: int
) -> None:
    stmt = delete(User).where(and_(User.id == id_to_delete))
    await session.execute(stmt)