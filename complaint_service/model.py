from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import registry
from sqlalchemy import MetaData
from .schema import Complain
from .config import settings
from sqlalchemy import UniqueConstraint

metadata_obj = MetaData(naming_convention=settings.db.naming_convention)
mapper_registry = registry(metadata=metadata_obj)

complain_table = Table(
    "complain_table",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("who", String(30)),
    Column("whom", String(30)),
    Column("about", String(30)),
    Column("data", String(30)),
)

mapper_registry.map_imperatively(Complain, complain_table)
