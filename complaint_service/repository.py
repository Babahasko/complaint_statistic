from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, delete, ScalarResult, and_
from typing import Sequence, Any, Coroutine
from .schema import ComplainCreate
from .model import Complain
from .logger import logger

class ComplainRepository:
    @staticmethod
    async def insert_complains(
            session: AsyncSession,
            insert_complains: Sequence[ComplainCreate]
    ) -> ScalarResult[Complain]:
        insert_list = []
        for insert_complain in insert_complains:
            insert_list.append(insert_complain.model_dump())
        complains = await session.scalars(
            insert(Complain).returning(Complain),insert_list,
        )
        return complains

    @staticmethod
    async def select_all_complains(
            session: AsyncSession,
    ) -> Sequence[Complain]:
        stmt = select(Complain).order_by(Complain.data.desc())
        result = await session.scalars(stmt)
        return result.all()

    @staticmethod
    async def delete_complain(
            session: AsyncSession,
            id_to_delete: int
    ) -> None:
        stmt = delete(Complain).where(and_(Complain.id == id_to_delete))
        await session.execute(stmt)

    @staticmethod
    async def update_complain(self):
        pass

#     async def delete_complain(
#             async_session: async_sessionmaker[AsyncSession],
#             complain_id: int
#     ) -> str:
#         async with async_session() as session:
#             async with session.begin():
#                 complain_to_delete = await session.get(Complain, complain_id)
#
#                 await session.delete(complain_to_delete)
#                 await session.commit()
#         # complain_delete = session.get(Complain, complain_id)
#         # await session.delete(complain_delete)
#         # await session.commit()
#         return f'complain deleted sucessfully'
