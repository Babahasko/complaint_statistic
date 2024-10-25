from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, delete

from core.models import Complain
from core.schemas.complain import ComplainCreate
from core.utils import logger


async def add_complain(
    session: AsyncSession, insert_complain: ComplainCreate
) -> Complain:
    complain_dict = insert_complain.model_dump()
    complain_result = await session.scalars(
        insert(Complain).returning(Complain), [complain_dict]
    )
    complain = complain_result.one()
    logger.info(f"complain_created = {complain}")
    return complain


async def delete_complain_by_id(session: AsyncSession, complain_id: int) -> str:
    stmt = delete(Complain).where(Complain.id == complain_id)
    await session.execute(stmt)
    logger.info(f"Complain with id: {complain_id} deleted successfully")
