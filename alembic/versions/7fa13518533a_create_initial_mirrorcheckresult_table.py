"""Create initial mirrorcheckresult table

Revision ID: 7fa13518533a
Revises: 
Create Date: 2017-02-10 20:47:01.467748

"""

# revision identifiers, used by Alembic.
revision = '7fa13518533a'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mirrorcheckresult',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('site', sa.String(), nullable=False),
    sa.Column('last_test', sa.DateTime(), nullable=False),
    sa.Column('last_noerror', sa.DateTime(), nullable=True),
    sa.Column('trace_master_timestamp', sa.DateTime(), nullable=True),
    sa.Column('error', sa.String(), nullable=True),
    sa.Column('warning', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('site')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mirrorcheckresult')
    ### end Alembic commands ###