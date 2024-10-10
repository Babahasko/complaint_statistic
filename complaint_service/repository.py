from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, ScalarResult
from typing import Sequence, Any, Coroutine
from .schema import Complain
from .model import ComplainORM
from .logger import logger

class ComplainRepository:
    @staticmethod
    async def insert_complains(
            session: AsyncSession,
            insert_complains: Sequence[Complain]
    ) -> ScalarResult[ComplainORM]:
        insert_list = []
        for insert_complain in insert_complains:
            insert_list.append(insert_complain.model_dump())
        complains = await session.scalars(
            insert(ComplainORM).returning(ComplainORM),insert_list,
        )
        return complains

    @staticmethod
    async def select_all_complains(
            session: AsyncSession,
    ) -> Sequence[ComplainORM]:
        stmt = select(ComplainORM).order_by(ComplainORM.data.desc())
        result = await session.scalars(stmt)
        return result.all()

    @staticmethod
    async def delete_complain(
            session: AsyncSession,
    ) -> None:
        stmt = select(ComplainORM).order_by(ComplainORM.data.desc()).limit(1)
        deleting_complain = await session.scalars(stmt)
        await session.delete(deleting_complain)

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
