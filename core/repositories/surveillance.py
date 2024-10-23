from sqlalchemy.ext.asyncio import AsyncSession, AsyncResult
from sqlalchemy import select, insert, delete, update, and_
from core.schemas.surveillance import SurveillanceCreate

from core.models import User
from core.models import Surveillance

from core.utils import logger


async def create_surveillance(
    session: AsyncSession, insert_surveillance: SurveillanceCreate
) -> Surveillance:
    surveillance_dict = insert_surveillance.model_dump()
    surveillance_result = await session.scalars(
        insert(Surveillance).returning(Surveillance), [surveillance_dict]
    )
    surveillance = surveillance_result.one()
    logger.info(f"surveillance created {surveillance}")
    return surveillance
