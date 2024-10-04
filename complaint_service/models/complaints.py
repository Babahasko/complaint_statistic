from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Complain(Base):
    __tablename__ = "user_complaints"
    id: Mapped[int] = mapped_column(primary_key=True)

    who: Mapped[str] = mapped_column(String(30))
    about: Mapped[str] = mapped_column(String(30))
    whom: Mapped[str] = mapped_column(String(30))
    data: Mapped[datetime]

    def __repr__(self) -> str:
        return (
            f"UserComplain(id={self.id!r}, who_complain={self.who!r}, complain_about={self.about!r},"
            f"to_whom_complain={self.whom}, data={self.data})")
