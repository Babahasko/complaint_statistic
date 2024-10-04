from complaint_service import current_db
from complaint_service import db_helper
from complaint_service.models import Base, Complain
from complaint_service.crud import get_complains, create_complain, delete_complain
from loguru import logger
from datetime import datetime
import asyncio
import sys

from complaint_service.schemas.complain import ComplainCreate

logger.remove()
logger.add(sys.stderr,enqueue=True, level = 'DEBUG')

async def main() -> None:
    logger.info("Sync db")
    engine = current_db.engine
    async_session = db_helper.current_db.session_factory
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
# Пример добавления объекта в бд
    example_1 = ComplainCreate(
        who='Старый',
        about='жизнь',
        whom='Даня',
        data=datetime.now(),
    )
    await create_complain(async_session,example_1)
# Приме удаления объекта из бд
    await delete_complain(async_session, 11)
# Пример получения всех записей в БД
    result = await get_complains(async_session)
    logger.info(f"Result = {result}")

    await current_db.engine.dispose()


if __name__ == '__main__':
    asyncio.run(main())