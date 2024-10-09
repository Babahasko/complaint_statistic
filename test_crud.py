import pytest
from complaint_service.schema import Complain
from complaint_service.db_helper import db_helper
from complaint_service.repository import ComplainRepository
from complaint_service.logger import logger
from datetime import datetime


@pytest.mark.asyncio
async def test_writing_and_reding_from_db():
    logger.info('Starting testing creating')
    time = datetime.now()
    complain = Complain(who='Дед', whom='Мирон', about='Колени', data=time)
    async_generator = db_helper.session_getter()
    async_session = await anext(async_generator)
    logger.info(f'async_session = {async_session.__dict__}')
    logger.info(f'complain = {complain}')
    await ComplainRepository.create_complain(session=async_session, complain=complain)
    await db_helper.dispose()

@pytest.mark.asyncio
async def test_reading_from_db():
    logger.info('Starting testing reading')
    async_generator = db_helper.session_getter()
    async_session = await anext(async_generator)
    result = await ComplainRepository.select_all_complaints(session=async_session)
    logger.info(f'result_reading_from_db = {result}')
    await db_helper.dispose()

# @pytest.mark.asyncio
# async def test_deleting_from_db():
#     logger.info('Start testing deleting')
#     async_generator = db_helper.session_getter()
#     async_session = await anext(async_generator)
#     result = await ComplainRepository.delete_complain(session=async_session)
#     logger.info(f'result_deleting_from_db = {result}')
#     await db_helper.dispose()
