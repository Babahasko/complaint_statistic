import random

import pytest

from datetime import datetime

from core.schemas import (
    UserCreate,
    ThemeCreate,
    SurveillanceCreate,
    ComplainCreate,
    UserUpdate,
    ThemeUpdate,
    SurveillanceUpdate,
)
from core.utils import logger

from core.crud import user as user_crud
from core.crud import theme as theme_crud
from core.crud import surveillance as surveillance_crud
from core.crud import complain as complain_crud

from help_functions import get_random_user


@pytest.mark.asyncio()
async def test_create_user(async_session, telegramm_account_factory, username_factory):
    telegramm_account_name = telegramm_account_factory()
    username = username_factory()
    user_schema = UserCreate(
        username=username, telegramm_account=telegramm_account_name
    )
    user = await user_crud.add_user(
        session=async_session,
        insert_user=user_schema,
    )
    assert user_schema.username == user.username
    assert user_schema.telegramm_account == user.telegramm_account


@pytest.mark.asyncio()
async def test_select_all_users(async_session):
    all_users = await user_crud.get_all_users(session=async_session)
    logger.info(f"{all_users}")


@pytest.mark.asyncio()
async def test_create_theme_by_user(async_session, theme_factory):
    random_user = await get_random_user(async_session)
    theme_name = theme_factory()
    theme_create = ThemeCreate(name=theme_name, user_id=random_user.id)
    theme = await theme_crud.add_theme(session=async_session, insert_theme=theme_create)
    logger.info(f"{theme}")


@pytest.mark.asyncio()
async def test_create_surveillance_by_user(async_session, surveillance_factory):
    random_user = await get_random_user(async_session)
    surveillance_name = surveillance_factory()
    surveillance_create = SurveillanceCreate(
        name=surveillance_name, user_id=random_user.id
    )
    surveillance = await surveillance_crud.add_surveillance(
        session=async_session, insert_surveillance=surveillance_create
    )
    logger.info(f"{surveillance}")


@pytest.mark.asyncio()
async def test_user_create_theme_and_get_them(async_session):
    random_user = await get_random_user(async_session)
    theme_1 = ThemeCreate(name="Свобода", user_id=random_user.id)
    theme_2 = ThemeCreate(name="Равенство", user_id=random_user.id)
    theme_3 = ThemeCreate(name="Братство", user_id=random_user.id)
    all_themes = [theme_1, theme_2, theme_3]
    for theme in all_themes:
        await theme_crud.add_theme(session=async_session, insert_theme=theme)

    user_with_themes = await user_crud.get_user_themes(
        session=async_session, user_id=random_user.id
    )
    logger.info(f"{user_with_themes.themes}")


@pytest.mark.asyncio()
async def test_user_create_surveillance_and_get_them(async_session):
    random_user = await get_random_user(async_session)
    surveillance_1 = SurveillanceCreate(name="Чимин", user_id=random_user.id)
    surveillance_2 = SurveillanceCreate(name="Чонгук", user_id=random_user.id)
    surveillance_3 = SurveillanceCreate(name="Тэхён", user_id=random_user.id)
    all_surveillances = [surveillance_1, surveillance_2, surveillance_3]
    for surveillance in all_surveillances:
        await surveillance_crud.add_surveillance(
            session=async_session, insert_surveillance=surveillance
        )

    user_with_surveillances = await user_crud.get_user_surveillance(
        session=async_session, user_id=random_user.id
    )
    logger.info(f"{user_with_surveillances.surveillance}")


@pytest.mark.asyncio()
async def test_user_create_complain_and_get_them(async_session):
    random_user = await get_random_user(async_session)

    theme_1 = ThemeCreate(name="Свобода", user_id=random_user.id)
    theme_2 = ThemeCreate(name="Равенство", user_id=random_user.id)
    theme_3 = ThemeCreate(name="Братство", user_id=random_user.id)
    all_themes = [theme_1, theme_2, theme_3]
    for theme in all_themes:
        await theme_crud.add_theme(session=async_session, insert_theme=theme)

    user_with_themes = await user_crud.get_user_themes(
        session=async_session, user_id=random_user.id
    )
    random_theme = random.choice(user_with_themes.themes)
    logger.info(f"{random_theme}")

    surveillance_1 = SurveillanceCreate(name="Чимин", user_id=random_user.id)
    surveillance_2 = SurveillanceCreate(name="Чонгук", user_id=random_user.id)
    surveillance_3 = SurveillanceCreate(name="Тэхён", user_id=random_user.id)
    all_surveillances = [surveillance_1, surveillance_2, surveillance_3]
    for surveillance in all_surveillances:
        await surveillance_crud.add_surveillance(
            session=async_session, insert_surveillance=surveillance
        )

    user_with_surveillance = await user_crud.get_user_surveillance(
        session=async_session, user_id=random_user.id
    )
    random_surveillance = random.choice(user_with_surveillance.surveillance)
    logger.info(f"{random_surveillance}")

    data = datetime.now()

    complain_create = ComplainCreate(
        user_id=random_user.id,
        theme_id=random_theme.id,
        surveillance_id=random_surveillance.id,
        data=data,
    )

    created_complain = await complain_crud.add_complain(
        session=async_session, insert_complain=complain_create
    )
    logger.info(f"{created_complain}")


@pytest.mark.asyncio()
async def test_update_user_function(async_session):
    random_user = await get_random_user(async_session)
    update_user_values = UserUpdate(username="Густав")
    await user_crud.update_user_by_id(
        session=async_session,
        user=random_user,
        update_user_values=update_user_values,
    )


@pytest.mark.asyncio()
async def test_update_theme_function(async_session):
    random_user = await get_random_user(async_session)
    user_with_themes = await user_crud.get_user_themes(async_session, random_user.id)
    logger.info(f"user_with_themes = {user_with_themes.themes}")
    random_theme = random.choice(user_with_themes.themes)
    logger.info(f"random_theme = {random_theme}")
    update_theme = ThemeUpdate(name="Дороги")
    await theme_crud.update_theme_by_user(
        session=async_session,
        theme=random_theme,
        user=random_user,
        update_theme_values=update_theme,
    )


@pytest.mark.asyncio()
async def test_update_surveillance_function(async_session):
    random_user = await get_random_user(async_session)
    user_with_surveillance = await user_crud.get_user_surveillance(
        async_session, random_user.id
    )
    logger.info(f"user_with_themes = {user_with_surveillance.surveillance}")
    random_surveillance = random.choice(user_with_surveillance.surveillance)
    logger.info(f"random_surveillance = {random_surveillance}")
    update_surveillance_values = SurveillanceUpdate(name="Яков")
    await surveillance_crud.update_surveillance_by_user(
        session=async_session,
        surveillance=random_surveillance,
        user=random_user,
        update_surveillance_values=update_surveillance_values,
    )