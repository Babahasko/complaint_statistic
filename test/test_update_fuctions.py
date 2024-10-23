import pytest

from help_functions import select_random_user
from core.repositories import user as user_crud
from core.schemas import UserUpdate
from core.utils import logger


@pytest.mark.asyncio()
async def test_update_user_function(async_session):
    random_user = await select_random_user(async_session)
    update_user_values = UserUpdate(username="Густав")
    await user_crud.update_user(
        session=async_session,
        user=random_user,
        update_user_values=update_user_values,
    )
