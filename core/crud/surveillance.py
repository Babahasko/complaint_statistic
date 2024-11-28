from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.mysql import insert
from sqlalchemy import delete, select
from core.schemas.surveillance import SurveillanceCreate, SurveillanceUpdate

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


async def get_all_surveillances(
    session: AsyncSession,
) -> Sequence[Surveillance]:
    stmt = select(Surveillance)
    surveillances = await session.scalars(stmt)
    all_surveillances = surveillances.all()
    logger.info(f"list_all_surveillances = {all_surveillances}")
    return all_surveillances

async def get_surveillance_by_name(
    session: AsyncSession,
    name: str,
) -> Surveillance:
    stmt = select(Surveillance).where(Surveillance.name == name)
    surveillance_selected_by_name = await session.scalars(stmt)
    result = surveillance_selected_by_name.one()
    logger.info(f"surveillance_selected_by_name = {result}")
    return result

async def get_surveillance_by_user(
    session: AsyncSession,
    user_id: int,
) -> Sequence[Surveillance]:
    stmt = select(Surveillance).where(Surveillance.user_id == user_id)
    surveillance_selected_by_user = await session.scalars(stmt)
    result = surveillance_selected_by_user.all()
    logger.info(f"surveillance_selected_by_user = {result}")
    return result

async def update_surveillance(
    session: AsyncSession,
    surveillance: Surveillance,
    update_surveillance_values: SurveillanceUpdate,
) -> None:
    update_surveillance_dict = update_surveillance_values.model_dump()
    insert_stmt = insert(Surveillance).values(
        id=surveillance.id,
        name=update_surveillance_dict["name"],
        user_id=surveillance.user_id,
    )
    on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
        name=insert_stmt.inserted.name,
    )
    await session.execute(on_duplicate_key_stmt)
    logger.info(f"Surveillance with id: {surveillance.id} updated successfully")


async def delete_surveillance_by_id(
    session: AsyncSession,
    surveillance_id: int,
) -> str:
    stmt = delete(Surveillance).where(Surveillance.id == surveillance_id)
    await session.execute(stmt)
    logger.info(f"Surveillance with id: {surveillance_id} deleted successfully")
    await session.commit()
