import pytest
from complaint_service.schema import Complain
from complaint_service.db_helper import db_helper
from complaint_service.repository import ComplainRepository
from complaint_service.logger import logger
from datetime import datetime


@pytest.mark.asyncio
async def test_writing_and_reding_from_db(session):
    logger.info('Starting testing creating in new_db')
    time = datetime.now()
    complain = Complain(who='Дед', whom='Мирон', about='Колени', data=time)
    logger.info(f'complain = {complain}')
    await ComplainRepository.create_complain(session=session, complain=complain)
    await db_helper.dispose()
