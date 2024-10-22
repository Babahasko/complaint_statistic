import pytest
from core.utils.db_helper import db_helper

from core.schemas import UserCreate, ThemeCreate, SurveillanceCreate
from core.utils import logger

from core.repositories import user as user_crud
from core.repositories import theme as theme_crud
from core.repositories import surveillance as surveillance_crud


@pytest.mark.asyncio()
async def test_create_user(async_session, telegramm_account_factory):
    telegramm_names = telegramm_account_factory(1)
    logger.info(f"{telegramm_names[0]}")
    user_schema = UserCreate(username="Gerbert", telegramm_account=telegramm_names[0])

    user = await user_crud.create_user(
        session=async_session,
        insert_user=user_schema,
    )
    logger.info(f"{user}")


@pytest.mark.asyncio()
async def test_select_user(async_session):
    user = await user_crud.select_user_by_username(
        session=async_session, username="Gerbert"
    )
    logger.info(user)


@pytest.mark.asyncio()
async def test_create_theme_by_user(async_session):

    user = await user_crud.select_user_by_username(
        session=async_session, username="Gerbert"
    )
    logger.info(user)
    theme_create = ThemeCreate(name="Mark2 и сжатие пространства", user_id=user.id)
    theme = await theme_crud.create_theme(
        session=async_session, insert_theme=theme_create
    )
    logger.info(f"{theme}")


@pytest.mark.asyncio()
async def test_create_surveillance_by_user(async_session):
    user = await user_crud.select_user_by_username(
        session=async_session, username="Gerbert"
    )
    logger.info(user)
    surveillance_create = SurveillanceCreate(name="Объект_1", user_id=user.id)
    surveillance = await surveillance_crud.create_surveillance(
        session=async_session, insert_surveillance=surveillance_create
    )
    logger.info(f"{surveillance}")
