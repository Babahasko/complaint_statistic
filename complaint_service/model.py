from sqlalchemy import String, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from .config import settings

class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention = settings.db.naming_convention
    )

class ComplainORM(Base):
    __tablename__ = 'complain_table'
    id: Mapped[int] = mapped_column(primary_key = True)
    who: Mapped[str] = mapped_column(String(30))
    whom: Mapped[str] = mapped_column(String(30))
    about: Mapped[str] = mapped_column(String(30))
    data: Mapped[datetime] = mapped_column(DateTime)

    def __repr__(self):
        return f'Complain(id={self.id}, who={self.who}, about={self.about}, whom={self.whom}, data={self.data})'

