import pytest
from complaint_service.schema import Complain
from complaint_service.db_helper import db_helper
from complaint_service.repository import ComplainRepository
from complaint_service.logger import logger
from datetime import datetime

@pytest.mark.asyncio
async def test_writing_and_reding_from_db(async_session):
    logger.info('Starting testing creating')
    time = datetime.now()
    complain = Complain(who='Дед', whom='Мирон', about='Колени', data=time)
    logger.info(f'complain = {complain}')
    # async_session = db_helper.session_factory()
    await ComplainRepository.create_complain(session=async_session, complain=complain)
    result = await ComplainRepository.select_all_complaints(session=async_session)
    logger.info(f'result select = {result[0]}')
    assert result[0].data.strftime("%Y-%m-%d %H:%M:%S") == complain.data.strftime("%Y-%m-%d %H:%M:%S")
    await db_helper.dispose()
