from sqlalchemy import String
from sqlalchemy.orm import  Mapped, mapped_column
from sqlalchemy import DateTime
from datetime import datetime
from .base import Base


class Complain(Base):
    __tablename__ = 'complain_table'
    id: Mapped[int] = mapped_column(primary_key = True)
    who: Mapped[str] = mapped_column(String(30))
    sender: Mapped[str] = mapped_column(String(30))
    about: Mapped[str] = mapped_column(String(30))
    data: Mapped[datetime] = mapped_column(DateTime)

    def __repr__(self):
        return f'Complain(id={self.id}, who={self.who}, about={self.about}, sender={self.sender}, data={self.data})'

