from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime
from sqlalchemy import DateTime

from .base import Base
from .user import User
from .surveillance import Surveillance
from .theme import Theme


class Complain(Base):
    __tablename__ = "complain_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    user: Mapped["User"] = relationship(back_populates="complains")
    surveillance_id: Mapped[int] = mapped_column(ForeignKey("surveillance_table.id"))
    surveillance: Mapped["Surveillance"] = relationship(back_populates="complains")
    theme_id: Mapped[int] = mapped_column(ForeignKey("theme_table.id"))
    theme: Mapped["Theme"] = relationship(back_populates="complains")
    data: Mapped[datetime] = mapped_column(DateTime)

    def __repr__(self):
        return f"Complain(id={self.id}, user={self.user}, theme={self.theme}, data={self.data})"
