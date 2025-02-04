"""empty message

Revision ID: 9325aa369e3c
Revises: 94e9a7b167e3
Create Date: 2019-07-24 19:19:16.136570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9325aa369e3c'
down_revision = '94e9a7b167e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('disease_stage_id_fkey', 'disease', type_='foreignkey')
    op.drop_column('disease', 'stage_id')
    op.add_column('stage', sa.Column('disease_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'stage', 'disease', ['disease_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'stage', type_='foreignkey')
    op.drop_column('stage', 'disease_id')
    op.add_column('disease', sa.Column('stage_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('disease_stage_id_fkey', 'disease', 'stage', ['stage_id'], ['id'])
    # ### end Alembic commands ###
