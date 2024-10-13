from sqlalchemy.orm import DeclarativeBase
from core.config import settings
from sqlalchemy import MetaData

class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention = settings.db.naming_convention
    )
