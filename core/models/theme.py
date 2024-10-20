from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from .base import Base

if TYPE_CHECKING:
    from .user import User
    from .complain import Complain

class Theme(Base):
    __tablename__ = "theme_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    user: Mapped["User"] = relationship(back_populates="themes")
    complains: Mapped[["Complain"]] = relationship(back_populates="theme")

    def __repr__(self):
        return f"Theme(name={self.name})"
