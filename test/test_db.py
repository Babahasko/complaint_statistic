import pytest
from complaint_service.schema import Complain
from complaint_service.db_helper import db_helper
from complaint_service.repository import ComplainRepository
from complaint_service.logger import logger
from datetime import datetime

@pytest.mark.asyncio()
async def test_writing_and_reding_from_db(async_session, complains_factory):
    logger.info('Starting testing creating')
    complains = complains_factory(3)
    logger.info(f'complain = {complains}')
    await ComplainRepository.insert_complains(session=async_session, insert_complains=complains)
    result = await ComplainRepository.select_all_complains(session=async_session)
    logger.info(f'result insert = {complains[0]}')
    logger.info(f'result select = {result[0]}')
    assert result[0].data.strftime("%Y-%m-%d %H:%M:%S") == complains[0].data.strftime("%Y-%m-%d %H:%M:%S")
    assert result[0].who == complains[0].who
    assert result[0].whom == complains[0].whom
    assert result[0].about == complains[0].about

