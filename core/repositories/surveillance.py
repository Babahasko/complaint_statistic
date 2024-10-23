from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.mysql import insert
from core.schemas.surveillance import SurveillanceCreate, SurveillanceUpdate

from core.models import User
from core.models import Surveillance

from core.utils import logger


async def add_surveillance(
    session: AsyncSession, insert_surveillance: SurveillanceCreate
) -> Surveillance:
    surveillance_dict = insert_surveillance.model_dump()
    surveillance_result = await session.scalars(
        insert(Surveillance).returning(Surveillance), [surveillance_dict]
    )
    surveillance = surveillance_result.one()
    logger.info(f"surveillance created {surveillance}")
    return surveillance


async def update_surveillance_by_user(
    session: AsyncSession,
    surveillance: Surveillance,
    user: User,
    update_surveillance_values: SurveillanceUpdate,
) -> None:
    update_surveillance_dict = update_surveillance_values.model_dump()
    insert_stmt = insert(Surveillance).values(
        id=surveillance.id, name=update_surveillance_dict["name"], user_id=user.id
    )
    on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
        name=insert_stmt.inserted.name,
    )
    await session.execute(on_duplicate_key_stmt)
