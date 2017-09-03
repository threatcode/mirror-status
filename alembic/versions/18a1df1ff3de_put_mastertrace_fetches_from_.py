"""Put mastertrace fetches from siteAliases into the db

Revision ID: 18a1df1ff3de
Revises: e28072a46d54
Create Date: 2017-09-03 13:48:30.733772

"""

# revision identifiers, used by Alembic.
revision = '18a1df1ff3de'
down_revision = 'e28072a46d54'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sitealiasmastertrace',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sitealias_id', sa.Integer(), nullable=False),
    sa.Column('checkrun_id', sa.Integer(), nullable=False),
    sa.Column('full', sa.String(), nullable=True),
    sa.Column('trace_timestamp', sa.DateTime(timezone=True), nullable=True),
    sa.Column('error', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['checkrun_id'], ['checkrun.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sitealias_id'], ['sitealias.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sitealiasmastertrace_checkrun_id'), 'sitealiasmastertrace', ['checkrun_id'], unique=False)
    op.create_index(op.f('ix_sitealiasmastertrace_sitealias_id'), 'sitealiasmastertrace', ['sitealias_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sitealiasmastertrace_sitealias_id'), table_name='sitealiasmastertrace')
    op.drop_index(op.f('ix_sitealiasmastertrace_checkrun_id'), table_name='sitealiasmastertrace')
    op.drop_table('sitealiasmastertrace')
    ### end Alembic commands ###