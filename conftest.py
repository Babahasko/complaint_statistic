from typing import Sequence

import pytest
import pytest_asyncio
from complaint_service.db_helper import DatabaseHelper
from complaint_service.model import Base
from complaint_service.schema import Complain
from complaint_service.logger import logger
from complaint_service.db_helper import db_helper
from datetime import datetime
import random

@pytest_asyncio.fixture
async def async_session():
    async with db_helper.session_factory() as session:
        yield session


person = ['Дед', 'Мирон', 'Земеля', 'Колян']
about_themes = ['Колени', 'Жизнь', 'Жена', 'Работа', 'Машина']


@pytest.fixture
def get_complains(number: int) -> Sequence[Complain]:
    list_complains = []
    for i in range (number):
        time = datetime.now()
        who = random.choice(person)
        person_without_who = [p for p in person if p != who]
        whom = random.choice(person_without_who)
        about = random.choice(about_themes)
        complain = Complain(who=who, whom=whom, about=about, data=time)
        list_complains.append(complain)
    return list_complains

#     db_helper = DatabaseHelper(
#         url="sqlite:///:memory:",
#     )
#     Base.metadata.create_all(db_helper.engine)
#
#     yield session
#     await session.close()
#     Base.metadata.drop_all(db_helper.engine)
