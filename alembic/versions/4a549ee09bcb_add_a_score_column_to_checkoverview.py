"""Add a score column to checkoverview

Revision ID: 4a549ee09bcb
Revises: 516c878785c1
Create Date: 2017-08-29 13:59:35.231496

"""

# revision identifiers, used by Alembic.
revision = '4a549ee09bcb'
down_revision = '516c878785c1'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('checkoverview', sa.Column('score', sa.Float(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('checkoverview', 'score')
    ### end Alembic commands ###
