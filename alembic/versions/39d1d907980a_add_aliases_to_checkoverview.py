"""Add aliases to Checkoverview

Revision ID: 39d1d907980a
Revises: 18a1df1ff3de
Create Date: 2017-09-03 19:18:19.362626

"""

# revision identifiers, used by Alembic.
revision = '39d1d907980a'
down_revision = '18a1df1ff3de'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('checkoverview', sa.Column('aliases', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('checkoverview', 'aliases')
    ### end Alembic commands ###