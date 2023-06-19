"""create notes table

Revision ID: 90973b7f906f
Revises: 
Create Date: 2023-06-16 17:03:07.132371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90973b7f906f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "notes",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("text", sa.String),
        sa.Column("completed", sa.Boolean)
    )


def downgrade() -> None:
    op.drop_table("notes")
