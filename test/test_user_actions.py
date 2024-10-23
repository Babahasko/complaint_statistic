import pytest
import asyncio

from core.utils import logger
from core.schemas import UserCreate, ThemeCreate

from core.crud import user as user_crud
from core.crud import theme as theme_crud
from core.crud import surveillance as surveillance_crud
from core.crud import complain as complain_crud


@pytest.mark.asyncio()
async def test_user_create_theme(async_session):
    user_to_create = UserCreate(username="Unkle Martin", telegramm_account="@martinlsp")
    user = await user_crud.add_user(async_session, user_to_create)

    theme_to_create_1 = ThemeCreate(name="Налоги", user_id=user.id)
    theme_to_create_2 = ThemeCreate(name="Работа", user_id=user.id)
    theme_1 = await theme_crud.add_theme(async_session, theme_to_create_1)
    theme_2 = await theme_crud.add_theme(async_session, theme_to_create_2)

    assert theme_1.name == theme_to_create_1.name
    assert theme_2.name == theme_to_create_2.name


@pytest.mark.asyncio()
async def test_user_get_theme(async_session):
    user = await user_crud.get_user_by_username(async_session, username="Unkle Martin")
    user_themes = await user_crud.get_user_themes(async_session, user_id=user.id)


@pytest.mark.asyncio()
async def test_user_delete_theme():
    await asyncio.sleep(0.1)
    pass


@pytest.mark.asyncio()
async def test_user_create_surveillance():
    await asyncio.sleep(0.1)
    pass


@pytest.mark.asyncio()
async def test_user_get_surveillance():
    await asyncio.sleep(0.1)
    pass


@pytest.mark.asyncio()
async def test_user_delete_surveillance():
    await asyncio.sleep(0.1)
    pass


@pytest.mark.asyncio()
async def test_user_create_complain():
    await asyncio.sleep(0.1)
    pass


@pytest.mark.asyncio()
async def test_user_get_complains():
    await asyncio.sleep(0.1)
    pass


@pytest.mark.asyncio()
async def test_user_delete_complain():
    await asyncio.sleep(0.1)
    pass
