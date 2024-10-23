import pytest

from help_functions import select_random_user
from core.schemas import UserUpdate, ThemeUpdate, SurveillanceUpdate
from core.utils import logger

from core.repositories import user as user_crud
from core.repositories import theme as theme_crud
from core.repositories import surveillance as surveillance_crud
import random


@pytest.mark.asyncio()
async def test_update_user_function(async_session):
    random_user = await select_random_user(async_session)
    update_user_values = UserUpdate(username="Густав")
    await user_crud.update_user(
        session=async_session,
        user=random_user,
        update_user_values=update_user_values,
    )


@pytest.mark.asyncio()
async def test_update_theme_function(async_session):
    random_user = await select_random_user(async_session)
    user_with_themes = await user_crud.select_user_with_themes(
        async_session, random_user.id
    )
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
    random_user = await select_random_user(async_session)
    user_with_surveillance = await user_crud.select_user_with_surveillance(
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

@pytest.mark.asyncio()
async def test_update_complain_function(async_session):
    random_user = await select_random_user(async_session)
    user_with_complains = await user_crud.select_user_with_complains(
        async_session, random_user.id
    )
    logger.info(f"user_with_themes = {user_with_complains.complains}")
    random_complain = random.choice(user_with_complains.complains)
    logger.info(f"random_surveillance = {random_complain}")
    update_complain_values = ComplainUpdate()
    await complain_crud.update_complain_by_user(
        session=async_session,
        complain=random_complain,
        user=random_user,
        update_complain_values=update_complain_values,
    )
