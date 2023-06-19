"""update recipe models

Revision ID: 821213847011
Revises: 92a83394f729
Create Date: 2023-06-18 21:32:17.128311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '821213847011'
down_revision = '92a83394f729'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notes')
    op.add_column('recipes', sa.Column('name', sa.String(), nullable=True))
    op.add_column('recipes', sa.Column('ingredients', sa.ARRAY(sa.String()), nullable=True))
    op.add_column('recipes', sa.Column('description', sa.String(), nullable=True))
    op.drop_column('recipes', 'text')
    op.drop_column('recipes', 'completed')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('completed', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('recipes', sa.Column('text', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('recipes', 'description')
    op.drop_column('recipes', 'ingredients')
    op.drop_column('recipes', 'name')
    op.create_table('notes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('text', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('completed', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='notes_pkey')
    )
    # ### end Alembic commands ###