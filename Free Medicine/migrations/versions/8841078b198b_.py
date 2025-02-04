"""empty message

Revision ID: 8841078b198b
Revises: 7f1de97838ca
Create Date: 2019-07-25 14:07:50.924609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8841078b198b'
down_revision = '7f1de97838ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('diseases_stages',
    sa.Column('disease_id', sa.Integer(), nullable=True),
    sa.Column('stage_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['disease_id'], ['disease.id'], ),
    sa.ForeignKeyConstraint(['stage_id'], ['stage.id'], )
    )
    op.drop_constraint('stage_disease_id_fkey', 'stage', type_='foreignkey')
    op.drop_column('stage', 'disease_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stage', sa.Column('disease_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('stage_disease_id_fkey', 'stage', 'disease', ['disease_id'], ['id'])
    op.drop_table('diseases_stages')
    # ### end Alembic commands ###
