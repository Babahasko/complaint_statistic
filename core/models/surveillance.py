from typing import TYPE_CHECKING

#
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from .mixin import UserRelationMixin

if TYPE_CHECKING:
    from .complain import Complain


class Surveillance(UserRelationMixin, Base):
    __tablename__ = "surveillance_table"
    _user_back_populates = "surveillance"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(30))
    complains: Mapped[list["Complain"]] = relationship(back_populates="surveillance")

    def __repr__(self):
        return f"Surveillance(name={self.name})"
