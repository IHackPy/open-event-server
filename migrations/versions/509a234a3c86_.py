"""empty message

Revision ID: 509a234a3c86
Revises: eba5ba85d240
Create Date: 2016-10-15 18:52:30.378516

"""

# revision identifiers, used by Alembic.
revision = '509a234a3c86'
down_revision = 'eba5ba85d240'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('marketer_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'orders', 'user', ['marketer_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.drop_column('orders', 'marketer_id')
    ### end Alembic commands ###
