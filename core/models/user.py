from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from .base import Base

if TYPE_CHECKING:
    from .surveillance import Surveillance
    from .complain import Complain
    from .theme import Theme


class User(Base):
    __tablename__ = "user_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    telegramm_account: Mapped[str] = mapped_column(String(30), unique=True)
    username: Mapped[str] = mapped_column(String(30))
    surveillance: Mapped[list["Surveillance"]] = relationship(back_populates="user")
    complains: Mapped[list["Complain"]] = relationship(back_populates="user")
    themes: Mapped[list["Theme"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username}), telegramm_account={self.telegramm_account}"
