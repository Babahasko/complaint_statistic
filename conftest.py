from typing import Sequence, Callable

import pytest
import pytest_asyncio

from core.models.base import Base
from core.schemas.complain import ComplainCreate
from core.utils.db_helper import db_helper
from datetime import datetime
import random

@pytest_asyncio.fixture
async def async_session():
    async with db_helper.session_factory() as session:
        yield session
        await session.commit()
        await session.close()
        await db_helper.dispose()

@pytest.fixture
def complains_factory() -> Callable[[int], Sequence[ComplainCreate]]:
    person = ['Дед', 'Мирон', 'Зима', 'Колян']
    about_themes = ['Колени', 'Жизнь', 'Жена', 'Работа', 'Машина']
    def _complains(num_records: int) -> Sequence[ComplainCreate]:
        list_complains = []
        for _ in range (num_records):
            time = datetime.now()
            who = random.choice(person)
            person_without_who = [p for p in person if p != who]
            sender = random.choice(person_without_who)
            about = random.choice(about_themes)
            complain = ComplainCreate(who=who, sender=sender, about=about, data=time)
            list_complains.append(complain)
        return list_complains
    return _complains

#     db_helper = DatabaseHelper(
#         url="sqlite:///:memory:",
#     )
#     Base.metadata.create_all(db_helper.engine)
#
#     yield session
#     await session.close()
#     Base.metadata.drop_all(db_helper.engine)
