"""create table

Revision ID: bb26345318a8
Revises: 
Create Date: 2024-10-06 22:35:18.566321

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bb26345318a8"
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
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("complain_table")
