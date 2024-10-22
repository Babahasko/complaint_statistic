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
def telegramm_account_factory() -> Callable[[], str]:
    prefix_1_list = ["limon", "baskov", "mega", "alpha"]
    prefix_2_list = ["1", "2", "3", "4", "5", "6"]
    prefix_3_list = ["bs", "cs", "kz", "infer", "saber", "giga", "pilo"]
    prefix_4_list = ["kilo", "mili", "anter", "archi", "yandex", "mail", "outlook"]

    def _telegramm_account() -> str:
        prefix_1 = random.choice(prefix_1_list)
        prefix_2 = random.choice(prefix_2_list)
        prefix_3 = random.choice(prefix_3_list)
        prefix_4 = random.choice(prefix_4_list)
        telegramm_account_name = [prefix_1, prefix_2, prefix_3, prefix_4]
        result = "".join(telegramm_account_name)
        return result

    return _telegramm_account


@pytest.fixture()
def username_factory() -> Callable[[], str]:
    username_list = ["Антон", "Гена", "babi4", "Миша", "AlexDark", "Bandos", "Killah"]

    def _username() -> Sequence[str]:
        return random.choice(username_list)

    return _username


@pytest.fixture()
def theme_factory() -> Callable[[], str]:
    theme_list = ["Жизнь", "Работа", "Жена", "Машина", "ЖКХ", "Погода", "Начальство"]

    def _theme() -> Sequence[str]:
        return random.choice(theme_list)

    return _theme


@pytest.fixture()
def surveillance_factory() -> Callable[[], str]:
    surveillance_list = [
        "Объект_1",
        "Начальник",
        "Жена",
        "Лёха",
        "Антон",
        "Павел",
        "Гена",
    ]

    def _surveillance() -> Sequence[str]:
        return random.choice(surveillance_list)

    return _surveillance
