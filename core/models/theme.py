from typing import TYPE_CHECKING

from sqlalchemy import Mapped, mapped_column
from sqlalchemy import String, relationship


from .base import Base
from .user import User

if TYPE_CHECKING:
    from .complain import Complain
    from .user_theme_association import user_theme_association_table


class Theme(Base):
    __tablename__ = "theme_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    complains: Mapped[["Complain"]] = relationship(back_populates="theme")
    users: Mapped[list["User"]] = relationship(
        secondary=user_theme_association_table, back_populates="themes"
    )

    def __repr__(self):
        return f"Theme(id={self.id}, name={self.name}, complains={self.complains})"
