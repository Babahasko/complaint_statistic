import pytest
from core.repositories import user as user_crud
from core.schemas.user import UserCreate
from core.utils.logger import logger


@pytest.mark.asyncio()
async def test_insert_select_delete_user(async_session):
    logger.info("Start test_create_user")
    user = UserCreate(telegramm_account="@ponchik", name="Алексей")
    result_insert = await user_crud.create_user(async_session, user)
    logger.info(f"{result_insert}")
    # select_user_id = result_insert[0].id
    # logger.info(f'select_user_id = {select_user_id}')
    # result_select = await user_crud.select_user(async_session, select_user_id)
    # logger.info(f'{result_select}')
    # await user_crud.delete_complain(async_session, select_user_id)
    # result_after_delete = await user_crud.select_user(async_session, select_user_id)
    # assert result_after_delete == []


#
# @pytest.mark.asyncio()
# async def test_insert_update_delete_user(async_session):
#     logger.info("Start test_insert_update_delete_user")
#     user = UserCreate(telegramm_account="@blinchik", name="Мага")
#     result_insert = await user_crud.create_user(async_session, user)
#     logger.info(f"{result_insert[0]}")
#     select_user_id = result_insert[0].id
#     logger.info(f"select_user_id = {select_user_id}")
#     await user_crud.update_user_name(async_session, select_user_id, new_name="Васька")
#     user_after_update = await user_crud.select_user(async_session, select_user_id)
#     logger.info(f"{user_after_update}")
#     await user_crud.delete_complain(async_session, select_user_id)
#     result_after_delete = await user_crud.select_user(async_session, select_user_id)
#     assert result_after_delete == []
