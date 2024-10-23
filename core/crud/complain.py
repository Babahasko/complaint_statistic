from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

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
    logger.info(complain)
    return complain
