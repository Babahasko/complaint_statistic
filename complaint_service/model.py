from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import registry
from sqlalchemy import MetaData
from schema import Complain

mapper_registry = registry()

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
