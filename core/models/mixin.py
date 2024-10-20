from typing import TYPE_CHECKING
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from .user import User


class UserRelationMixin:
    _user_id_nullable = False
    _user_id_unique: bool = False
    _user_back_populates: str | None = None

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("user_table.id"),
            unique=cls._user_id_unique,
            nullable=cls._user_id_nullable,
        )

    @declared_attr
    def user(cls) -> Mapped["User"]:
        return relationship(
            back_populates=cls._user_back_populates,
        )
