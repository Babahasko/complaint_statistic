from core.repositories import user as user_crud
import random
from core.utils import logger


async def select_random_user(async_session):
    all_users = await user_crud.select_all_users(session=async_session)
    random_user = random.choice(all_users)
    logger.info(f"random_user = {random_user}")
    return random_user
