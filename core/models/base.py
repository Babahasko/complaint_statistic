from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from core.config import settings
from sqlalchemy import MetaData
from typing import List

from sqlalchemy import String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime
from datetime import datetime


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention
    )


class Complain(Base):
    __tablename__ = 'complain_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_table.id'))
    user: Mapped["User"] = relationship(back_populates='complains')
    surveillance_id: Mapped[int] = mapped_column(ForeignKey('surveillance_table.id'))
    surveillance: Mapped["Surveillance"] = relationship(back_populates='complains')
    theme_id: Mapped[int] = mapped_column(ForeignKey('theme_table.id'))
    theme: Mapped["Theme"] = relationship(back_populates='complains')
    data: Mapped[datetime] = mapped_column(DateTime)

    def __repr__(self):
        return f'Complain(id={self.id}, user={self.user}, theme={self.theme}, data={self.data})'


class Theme(Base):
    __tablename__ = 'theme_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    complains: Mapped[List[Complain]] = relationship(back_populates="theme")

    def __repr__(self):
        return f'Theme(id={self.id}, name={self.name}, complains={self.complains})'


user_themes_association_table = Table(
    "user_themes_association_table",
    Base.metadata,
    Column("user_id", ForeignKey("user_table.id"), primary_key=True),
    Column("theme_id", ForeignKey("theme_table.id"), primary_key=True),
)


class Surveillance(Base):
    __tablename__ = 'surveillance_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    complains: Mapped[List[Complain]] = relationship(back_populates="surveillance")
    user_id: Mapped[int] = mapped_column(ForeignKey('user_table.id'))
    user: Mapped["User"] = relationship(back_populates='surveillance')

    def __repr__(self):
        return f'Surveillance(id={self.id}, name={self.name}, complains={self.complains}, user={self.user})'


class User(Base):
    __tablename__ = 'user_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    telegramm_account: Mapped[str] = mapped_column(String(30), unique=True)
    name: Mapped[str] = mapped_column(String(30))
    surveillance: Mapped[List[Surveillance]] = relationship(back_populates='user')
    complains: Mapped[List[Complain]] = relationship(back_populates="user")
    themes: Mapped[List[Theme]] = relationship(secondary=user_themes_association_table)

    def __repr__(self):
        return (f'User(id={self.id},'
                f' telegramm_account={self.telegramm_account},'
                f' name={self.name},'
                )
