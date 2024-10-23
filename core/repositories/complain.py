from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, delete, ScalarResult, and_, Row
from typing import Sequence, Any

from core.models import Complain
from core.schemas.complain import ComplainCreate
from core.utils import logger


async def create_complain(
    session: AsyncSession, insert_complain: ComplainCreate
) -> Complain:
    complain_dict = insert_complain.model_dump()
    complain = await session.scalars(
        insert(Complain).returning(Complain), [complain_dict]
    )
    logger.info(f"complain created {complain.all()}")
    return complain.all()


#
# async def create_complains(
#         session: AsyncSession,
#         insert_complains: Sequence[ComplainCreate]
# ) -> ScalarResult[Complain]:
#     insert_list = []
#     for insert_complain in insert_complains:
#         insert_list.append(insert_complain.model_dump())
#     complains = await session.scalars(
#         insert(Complain).returning(Complain),insert_list,
#     )
#     result = complains.all()
#     return result
#
#
# async def select_all_complains(
#         session: AsyncSession,
# ) -> Sequence[Complain]:
#     stmt = select(Complain).order_by(Complain.data.asc())
#     result = await session.scalars(stmt)
#     return result.all()
#
#
# async def select_complains_by_id(
#         session: AsyncSession,
#         search_id: int
# ) -> Sequence[Row[Any]]:
#     stmt = select(Complain).where(Complain.id == search_id)
#     result = await session.scalars(stmt)
#     return result.all()
#
#
# async def delete_complain(
#         session: AsyncSession,
#         id_to_delete: int
# ) -> None:
#     stmt = delete(Complain).where(and_(Complain.id == id_to_delete))
#     await session.execute(stmt)
#
#
# async def update_complain():
#     pass
