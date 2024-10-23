import pytest

from core.crud.user import update_user_by_id
from core.schemas import UserCreate, UserUpdate
from core.crud import user as user_crud


@pytest.mark.asyncio()
async def test_create_user(async_session):
    user_to_create = UserCreate(username="John", telegramm_account="@JohnyXXX")
    created_user = await user_crud.add_user(async_session, user_to_create)
    assert created_user.username == "John"


@pytest.mark.asyncio()
async def test_update_user(async_session):
    user_update_values = UserUpdate(username="Bob")
    user_to_update = await user_crud.get_user_by_username(
        async_session, username="John"
    )
    await update_user_by_id(async_session, user_to_update, user_update_values)


@pytest.mark.asyncio()
async def test_delete_user(async_session):
    user_to_delete = await user_crud.get_user_by_username(async_session, username="Bob")
    await user_crud.delete_user_by_id(async_session, user_to_delete.id)
