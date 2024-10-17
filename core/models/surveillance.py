from typing import List

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from .complain import Complain
from .user import User


class Surveillance(Base):
    __tablename__ = "surveillance_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    complains: Mapped[List["Complain"]] = relationship(back_populates="surveillance")
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    user: Mapped["User"] = relationship(back_populates="surveillance")

    def __repr__(self):
        return f"Surveillance(id={self.id}, name={self.name}, complains={self.complains}, user={self.user})"
