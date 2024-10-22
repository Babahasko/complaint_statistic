from typing import Sequence, Callable

import pytest
import pytest_asyncio

from core.models.base import Base
from core.schemas.complain import ComplainCreate
from core.utils.db_helper import db_helper
from datetime import datetime
import random


@pytest_asyncio.fixture(scope="function")
async def async_session():
    async with db_helper.session_factory() as session:
        yield session
        await session.commit()
        await session.close()
        await db_helper.dispose()


@pytest.fixture()
def complains_factory() -> Callable[[int], Sequence[ComplainCreate]]:
    person = ["Дед", "Мирон", "Зима", "Колян"]
    about_themes = ["Колени", "Жизнь", "Жена", "Работа", "Машина"]

    def _complains(num_records: int) -> Sequence[ComplainCreate]:
        list_complains = []
        for _ in range(num_records):
            time = datetime.now()
            who = random.choice(person)
            person_without_who = [p for p in person if p != who]
            sender = random.choice(person_without_who)
            about = random.choice(about_themes)
            complain = ComplainCreate(who=who, sender=sender, about=about, data=time)
            list_complains.append(complain)
        return list_complains

    return _complains


@pytest.fixture()
def telegramm_account_factory() -> Callable[[int], Sequence[str]]:
    prefix_1_list = ["limon", "baskov", "mega", "alpha"]
    prefix_2_list = ["1", "2", "3", "4", "5", "6"]
    prefix_3_list = ["bs", "cs", "kz", "infer", "saber", "giga", "pilo"]
    prefix_4_list = ["kilo", "mili", "anter", "archi", "yandex", "mail", "outlook"]

    def _telegramm_account(num_records: int) -> Sequence[str]:
        list_telegramm_accounts = []
        for _ in range(num_records):
            prefix_1 = random.choice(prefix_1_list)
            prefix_2 = random.choice(prefix_2_list)
            prefix_3 = random.choice(prefix_3_list)
            prefix_4 = random.choice(prefix_4_list)
            telegramm_account_name = [prefix_1, prefix_2, prefix_3, prefix_4]
            result = "".join(telegramm_account_name)
            list_telegramm_accounts.append(result)
        return list_telegramm_accounts

    return _telegramm_account


#     db_helper = DatabaseHelper(
#         url="sqlite:///:memory:",
#     )
#     Base.metadata.create_all(db_helper.engine)
#
#     yield session
#     await session.close()
#     Base.metadata.drop_all(db_helper.engine)
