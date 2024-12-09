from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, delete, select
from sqlalchemy.orm import joinedload

from core.models import Complain
from core.schemas.complain import ComplainCreate, ComplainReadPretty
from core.utils import logger

from datetime import datetime


async def get_all_complains(
    session: AsyncSession,
) -> Sequence[Complain]:
    stmt = select(Complain)
    complains = await session.scalars(stmt)
    all_complains = complains.all()
    logger.info(f"list_all_complains = {all_complains}")
    return all_complains


async def get_complain_by_user(
    session: AsyncSession,
    user_id: int,
) -> Sequence[Complain]:
    stmt = select(Complain).where(Complain.user_id == user_id)
    complain_selected_by_user = await session.scalars(stmt)
    result = complain_selected_by_user.all()
    logger.info(f"complain_selected_by_user = {result}")
    return result

async def get_complain_by_user_pretty(
        session: AsyncSession,
        user_id: int
) -> Sequence[Complain]:
    stmt = select(Complain).where(Complain.user_id == user_id).options(
        joinedload(Complain.theme),
        joinedload(Complain.surveillance)
    )
    complain_selected_by_user = await session.scalars(stmt)
    bare_result = complain_selected_by_user.all()
    final_result = []
    for complain in bare_result:
        complain_read = ComplainReadPretty(
            id = complain.id,
            user_id = complain.user_id,
            theme_id = complain.theme_id,
            theme = complain.theme.name,
            surveillance_id = complain.surveillance_id,
            surveillance = complain.surveillance.name,
            data = complain.data
        )
        final_result.append(complain_read)
    return final_result



async def add_complain(
    session: AsyncSession, insert_complain: ComplainCreate
) -> Complain:
    complain_dict = insert_complain.model_dump()
    complain_dict["data"] = datetime.now()
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
    await session.commit()

