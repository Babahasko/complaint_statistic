from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from .mixin import UserRelationMixin

from .base import Base

if TYPE_CHECKING:
    from .complain import Complain


class Theme(UserRelationMixin, Base):
    __tablename__ = "theme_table"
    _user_back_populates = "themes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    complains: Mapped[["Complain"]] = relationship(back_populates="theme")

    def __repr__(self):
        return f"Theme(name={self.name})"
