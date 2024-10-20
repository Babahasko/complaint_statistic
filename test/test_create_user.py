import pytest
from core.utils.db_helper import db_helper

from core.schemas import UserCreate
from core.repositories import user as user_crud
from core.utils import logger


@pytest.mark.asyncio()
async def test_create_user():
    async with db_helper.session_factory() as session:
        user_schema = UserCreate(name="Bob", telegramm_account="@ponchik")
        user = await user_crud.create_user(
            session=session,
            insert_user=user_schema,
        )
        logger.info(f"{user}")
    # logger.info(f"{inserted_user}")
