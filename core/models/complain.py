from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from .mixin import UserRelationMixin

from .base import Base

if TYPE_CHECKING:
    from .surveillance import Surveillance
    from .theme import Theme


class Complain(UserRelationMixin, Base):
    __tablename__ = "complain_table"
    _user_back_populates = "complains"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[datetime] = mapped_column(DateTime)
    surveillance_id: Mapped[int] = mapped_column(ForeignKey("surveillance_table.id"))
    surveillance: Mapped["Surveillance"] = relationship(back_populates="complains")
    theme_id: Mapped[int] = mapped_column(ForeignKey("theme_table.id"))
    theme: Mapped["Theme"] = relationship(back_populates="complains")

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, data={self.data}), user={self.user}"
