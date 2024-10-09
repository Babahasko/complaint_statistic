import pytest
from complaint_service.db_helper import DatabaseHelper
from complaint_service.model import Base
from complaint_service.logger import logger

# @pytest.fixture
# async def session():
#     db_helper = DatabaseHelper(
#         url="sqlite:///:memory:",
#     )
#     Base.metadata.create_all(db_helper.engine)
#
#     yield session
#     await session.close()
#     Base.metadata.drop_all(db_helper.engine)
