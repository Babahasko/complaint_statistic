from loguru import logger
import asyncio
import sys

logger.remove()
logger.add(sys.stderr,enqueue=True, level = 'DEBUG')

async def main()-> None:
    await asyncio.sleep(3)


# async def main() -> None:
#     logger.info("Sync db")
#     engine = current_db.engine
#     async_session = db_helper.current_db.session_factory
#     # async with engine.begin() as conn:
#     #     await conn.run_sync(Base.metadata.create_all)
# # Пример добавления объекта в бд
#     example_1 = ComplainCreate(
#         who='Старый',
#         about='жизнь',
#         whom='Даня',
#         data=datetime.now(),
#     )
#     await create_complain(async_session,example_1)
# # Приме удаления объекта из бд
#     await delete_complain(async_session, 11)
# # Пример получения всех записей в БД
#     result = await get_complains(async_session)
#     logger.info(f"Result = {result}")
#
#     await current_db.engine.dispose()


if __name__ == '__main__':
    asyncio.run(main())