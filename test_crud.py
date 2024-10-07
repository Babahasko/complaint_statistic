import pytest
from complaint_service.schema import Complain
from complaint_service.db_helper import db_helper
from complaint_service.repository import ComplainRepository
from datetime import datetime

from loguru import logger
import asyncio
import sys

logger.remove()
logger.add(sys.stderr,enqueue=True, level = 'DEBUG')

@pytest.mark.asyncio
async def test_writing_in_db():
    time = datetime.now()
    complain = Complain(who='Дед', whom='Мирон', about='Колени', data=time)
    async_generator = db_helper.session_getter()
    async_session = await anext(async_generator)
    result = await ComplainRepository.add_complain(session=async_session, complain=complain)
    print(result)
    await db_helper.dispose()

    assert result == complain

