"""create complain table

Revision ID: a678d2f65413
Revises: 
Create Date: 2024-10-06 23:15:22.997276

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "a678d2f65413"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "complain_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("who", sa.String(length=30), nullable=True),
        sa.Column("whom", sa.String(length=30), nullable=True),
        sa.Column("about", sa.String(length=30), nullable=True),
        sa.Column("data", sa.String(length=30), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_complain_table")),
    )


def downgrade() -> None:
    op.drop_table("complain_table")
