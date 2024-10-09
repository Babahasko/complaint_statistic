import pytest
from complaint_service.db_helper import DatabaseHelper
from complaint_service.model import Base
from complaint_service.logger import logger
from complaint_service.db_helper import db_helper

@pytest.fixture
async def session():
    return db_helper.session_factory


#     db_helper = DatabaseHelper(
#         url="sqlite:///:memory:",
#     )
#     Base.metadata.create_all(db_helper.engine)
#
#     yield session
#     await session.close()
#     Base.metadata.drop_all(db_helper.engine)
