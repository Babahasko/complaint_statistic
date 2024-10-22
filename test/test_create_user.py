import random

import pytest
from core.utils.db_helper import db_helper

from core.schemas import UserCreate, ThemeCreate, SurveillanceCreate
from core.utils import logger

from core.repositories import user as user_crud
from core.repositories import theme as theme_crud
from core.repositories import surveillance as surveillance_crud


@pytest.mark.asyncio()
async def test_create_user(async_session, telegramm_account_factory, username_factory):
    telegramm_account_name = telegramm_account_factory()
    username = username_factory()
    user_schema = UserCreate(
        username=username, telegramm_account=telegramm_account_name
    )
    user = await user_crud.create_user(
        session=async_session,
        insert_user=user_schema,
    )
    logger.info(f"{user}")


@pytest.mark.asyncio()
async def test_select_all_users(async_session):
    all_users = await user_crud.select_all_users(session=async_session)
    logger.info(f"{all_users}")


@pytest.mark.asyncio()
async def test_select_user(async_session):
    all_users = await user_crud.select_all_users(session=async_session)
    random_user = random.choice(all_users)
    user = await user_crud.select_user_by_username(
        session=async_session, username=random_user.username
    )
    logger.info(user)


@pytest.mark.asyncio()
async def test_create_theme_by_user(async_session, theme_factory):
    all_users = await user_crud.select_all_users(session=async_session)
    random_user = random.choice(all_users)
    logger.info(f"{random_user}")
    theme_name = theme_factory()
    theme_create = ThemeCreate(name=theme_name, user_id=random_user.id)
    theme = await theme_crud.create_theme(
        session=async_session, insert_theme=theme_create
    )
    logger.info(f"{theme}")


@pytest.mark.asyncio()
async def test_create_surveillance_by_user(async_session, surveillance_factory):
    all_users = await user_crud.select_all_users(session=async_session)
    random_user = random.choice(all_users)
    logger.info(f"{random_user}")
    surveillance_name = surveillance_factory()
    surveillance_create = SurveillanceCreate(
        name=surveillance_name, user_id=random_user.id
    )
    surveillance = await surveillance_crud.create_surveillance(
        session=async_session, insert_surveillance=surveillance_create
    )
    logger.info(f"{surveillance}")
