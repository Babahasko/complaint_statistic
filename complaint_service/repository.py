from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Sequence
from .schema import Complain
from .model import ComplainORM
from .logger import logger


class ComplainRepository:
    @staticmethod
    async def create_complain(
            session: AsyncSession,
            complain: Complain
    ) -> ComplainORM:
        complain = ComplainORM(**complain.model_dump())
        logger.info(f'complain = {complain}')
        session.add(complain)
        await session.commit()
        return complain

    @staticmethod
    async def select_all_complaints(
            session: AsyncSession,
    ) -> Sequence[ComplainORM]:
        stmt = select(ComplainORM).order_by(ComplainORM.id)
        result = await session.scalars(stmt)
        await session.commit()
        return result.all()

    @staticmethod
    async def delete_complain(
            session: AsyncSession,
    ) -> None:
        stmt = select(ComplainORM).order_by(ComplainORM.id.desc()).limit(1)
        deleting_complain = await session.scalars(stmt)
        await session.delete(deleting_complain)
        await session.commit()

    @staticmethod
    async def update_complain(self):
        pass
# class ComplainRepository:
#     def __init__(self, async_session: async_sessionmaker[AsyncSession]):
#     async def get_complains(
#             async_session: self.async_session,
#     ) -> Sequence[Complain]:
#         async with async_session() as session:
#             async with session.begin():
#                 stmt = select(Complain).order_by(Complain.id)
#                 result = await session.scalars(stmt)
#         return result.all()
#
#
#     async def create_complain(
#             async_session: async_sessionmaker[AsyncSession],
#             complain_create: ComplainCreate
#     ) -> str:
#         async with async_session() as session:
#             async with session.begin():
#                 complain = Complain(**complain_create.model_dump())
#                 session.add(complain)
#         return f'Успешно внесено'
#
#
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
