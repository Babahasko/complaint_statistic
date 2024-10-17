from sqlalchemy import Table, Column, ForeignKey, Integer, UniqueConstraint
from .base import Base

user_theme_association_table = Table(
    "user_themes_association_table",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_table.id")),
    Column("theme_id", ForeignKey("theme_table.id")),
    UniqueConstraint("user_id", "theme_id"),
)
