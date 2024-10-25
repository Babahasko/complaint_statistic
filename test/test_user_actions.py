import pytest

from core.schemas import (
    UserCreate,
    ThemeCreate,
    SurveillanceCreate,
    ComplainCreate,
    ThemeUpdate,
    SurveillanceUpdate,
)

from core.crud import user as user_crud
from core.crud import theme as theme_crud
from core.crud import surveillance as surveillance_crud
from core.crud import complain as complain_crud
from datetime import datetime


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
async def test_user_update_theme(async_session):
    theme_update_values = ThemeUpdate(name="ЖКХ")
    theme_to_update = await theme_crud.get_theme_by_name(async_session, name="Налоги")
    await theme_crud.update_theme(
        async_session, theme=theme_to_update, update_theme_values=theme_update_values
    )


@pytest.mark.asyncio()
async def test_user_get_and_delete_theme(async_session):
    user = await user_crud.get_user_by_username(async_session, username="Unkle Martin")
    user_themes = await user_crud.get_user_themes(async_session, user_id=user.id)
    for user_theme in user_themes:
        assert user_theme.name in ("Работа", "ЖКХ")
    for theme in user_themes:
        await theme_crud.delete_theme_by_id(async_session, theme.id)
    await user_crud.delete_user_by_id(async_session, user.id)


@pytest.mark.asyncio()
async def test_user_create_surveillance(async_session):
    user_to_create = UserCreate(username="Unkle Martin", telegramm_account="@martinlsp")
    user = await user_crud.add_user(async_session, user_to_create)

    surveillance_to_create_1 = SurveillanceCreate(name="Боб", user_id=user.id)
    surveillance_to_create_2 = SurveillanceCreate(name="Мартин", user_id=user.id)
    surveillance_1 = await surveillance_crud.add_surveillance(
        async_session, surveillance_to_create_1
    )
    surveillance_2 = await surveillance_crud.add_surveillance(
        async_session, surveillance_to_create_2
    )

    assert surveillance_1.name == surveillance_to_create_1.name
    assert surveillance_2.name == surveillance_to_create_2.name


@pytest.mark.asyncio()
async def test_user_update_surveillance(async_session):
    surveillance_update_values = SurveillanceUpdate(name="Глеб")
    surveillance_to_update = await surveillance_crud.get_surveillance_by_name(
        async_session, name="Боб"
    )
    await surveillance_crud.update_surveillance(
        async_session,
        surveillance=surveillance_to_update,
        update_surveillance_values=surveillance_update_values,
    )


@pytest.mark.asyncio()
async def test_user_get_and_delete_surveillance(async_session):
    user = await user_crud.get_user_by_username(async_session, username="Unkle Martin")
    user_surveillances = await user_crud.get_user_surveillance(
        async_session, user_id=user.id
    )
    for user_surveillance in user_surveillances:
        assert user_surveillance.name in ("Глеб", "Мартин")
    for surveillance in user_surveillances:
        await surveillance_crud.delete_surveillance_by_id(
            async_session, surveillance.id
        )
    await user_crud.delete_user_by_id(async_session, user.id)


@pytest.mark.asyncio()
async def test_user_create_complain(async_session):
    user_to_create = UserCreate(username="Unkle Martin", telegramm_account="@martinlsp")
    user = await user_crud.add_user(async_session, user_to_create)

    theme_to_create = ThemeCreate(name="Здоровье", user_id=user.id)
    theme = await theme_crud.add_theme(async_session, insert_theme=theme_to_create)

    surveillance_to_create = SurveillanceCreate(name="Боб", user_id=user.id)
    surveillance = await surveillance_crud.add_surveillance(
        async_session, surveillance_to_create
    )

    complain_to_create_1 = ComplainCreate(
        user_id=user.id,
        theme_id=theme.id,
        surveillance_id=surveillance.id,
        data=datetime.now(),
    )
    complain_to_create_2 = ComplainCreate(
        user_id=user.id,
        theme_id=theme.id,
        surveillance_id=surveillance.id,
        data=datetime.now(),
    )
    complain_1 = await complain_crud.add_complain(async_session, complain_to_create_1)
    complain_2 = await complain_crud.add_complain(async_session, complain_to_create_2)

    assert complain_1.user_id == complain_to_create_1.user_id
    assert complain_1.theme_id == complain_to_create_1.theme_id
    assert complain_1.surveillance_id == complain_to_create_1.surveillance_id
    assert complain_1.data.strftime(
        "%d-%m-%Y %H:%M:%S"
    ) == complain_to_create_1.data.strftime("%d-%m-%Y %H:%M:%S")

    assert complain_2.user_id == complain_to_create_2.user_id
    assert complain_2.theme_id == complain_to_create_2.theme_id
    assert complain_2.surveillance_id == complain_to_create_2.surveillance_id
    assert complain_2.data.strftime(
        "%d-%m-%Y %H:%M:%S"
    ) == complain_to_create_2.data.strftime("%d-%m-%Y %H:%M:%S")


@pytest.mark.asyncio()
async def test_user_get_and_delete_complains(async_session):
    user = await user_crud.get_user_by_username(async_session, username="Unkle Martin")
    theme = await theme_crud.get_theme_by_name(async_session, name="Здоровье")
    surveillance = await surveillance_crud.get_surveillance_by_name(
        async_session, name="Боб"
    )
    user_complains = await user_crud.get_user_complains(async_session, user_id=user.id)
    for complain in user_complains:
        await complain_crud.delete_complain_by_id(async_session, complain.id)
    await theme_crud.delete_theme_by_id(async_session, theme.id)
    await surveillance_crud.delete_surveillance_by_id(async_session, surveillance.id)
    await user_crud.delete_user_by_id(async_session, user.id)
