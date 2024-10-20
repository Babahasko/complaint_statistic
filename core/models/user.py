from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

# from typing import List

from .base import Base

if TYPE_CHECKING:
    from .surveillance import Surveillance
    from .complain import Complain
    from .theme import Theme
#     from .user_theme_association import user_theme_association_table


class User(Base):
    __tablename__ = "user_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    telegramm_account: Mapped[str] = mapped_column(String(30), unique=True)
    username: Mapped[str] = mapped_column(String(30))
    surveillance: Mapped[list["Surveillance"]] = relationship(back_populates="user")
    complains: Mapped[list["Complain"]] = relationship(back_populates="user")
    themes: Mapped[list["Theme"]] = relationship(back_populates="user")
    # themes: Mapped[List["Theme"]] = relationship(
    #     secondary=user_theme_association_table,
    #     back_populates="users",
    # )

    def __repr__(self):
        return (
            f"User(id={self.id},"
            f" telegramm_account={self.telegramm_account},"
            f" name={self.username},"
        )
