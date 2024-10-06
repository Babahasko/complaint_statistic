"""create table

Revision ID: 5af2daae398d
Revises: 
Create Date: 2024-10-06 22:55:35.008182

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5af2daae398d"
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
