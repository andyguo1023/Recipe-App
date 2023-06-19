"""create recipes table

Revision ID: 92a83394f729
Revises: 90973b7f906f
Create Date: 2023-06-18 15:04:02.340794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92a83394f729'
down_revision = '90973b7f906f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "recipes",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("text", sa.String),
        sa.Column("completed", sa.Boolean)
    )


def downgrade() -> None:
    op.drop_table("recipes")
