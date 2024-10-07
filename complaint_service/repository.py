from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .schema import Complain


class ComplainRepository:
    @staticmethod
    async def add_complain(
            session: AsyncSession,
            complain: Complain
    ) -> Complain:
        complain = Complain(**complain.model_dump())
        session.add(complain)
        await session.commit()
        return complain

    @staticmethod
    async def get_complain(session: AsyncSession,
            complain: Complain
    ) -> Complain:
        pass
    async def delete_complain(self):
        pass
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
