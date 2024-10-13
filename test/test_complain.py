import pytest
from core.repositories import complain as complain_crud
from core.utils.logger import logger


@pytest.mark.asyncio()
async def test_get_complain_by_id(async_session):
    logger.info('Starting test_get_complain_by_id')
    select_all = await complain_crud.select_all_complains(async_session)
    select_id = select_all[-1].id
    result_select_by_id = await complain_crud.select_complains_by_id(async_session, select_id)
    logger.info(result_select_by_id)

@pytest.mark.asyncio()
async def test_bulk_insert_to_db(async_session, complains_factory):
    logger.info('Starting test_writing_and_reading_from_db')
    complains = complains_factory(10)
    logger.info(f'Добавляемые записи = {complains}')
    result_insert = await complain_crud.create_complains(session=async_session, insert_complains=complains)
    result_select = await complain_crud.select_all_complains(session=async_session)
    logger.info(f'Добавленные записи = {result_insert}')
    logger.info(f'Выбранные записи = {result_select}')
    for one_insert_result in result_insert:
        assert one_insert_result in result_select



# @pytest.mark.asyncio()
# async def test_delete_from_db(async_session):
#     logger.info('Starting testing deleting')
#     result = await ComplainRepository.select_all_complains(session=async_session)
#     id_to_delete = result[0].id
#     logger.info(f'id_to_delete = {id_to_delete}')
#     await ComplainRepository.delete_complain(async_session, id_to_delete)

