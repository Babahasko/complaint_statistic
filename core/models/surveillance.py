from typing import TYPE_CHECKING

#
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

if TYPE_CHECKING:
    from .user import User
    from .complain import Complain


class Surveillance(Base):
    __tablename__ = "surveillance_table"
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(30))
    complains: Mapped[list["Complain"]] = relationship(back_populates="surveillance")
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    user: Mapped["User"] = relationship(back_populates="surveillance")

    def __repr__(self):
        return f"Surveillance(name={self.name})"
