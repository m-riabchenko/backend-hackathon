"""empty message

Revision ID: 56b541071d1a
Revises: 51da20520d9a
Create Date: 2020-12-20 00:52:39.706397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56b541071d1a'
down_revision = '51da20520d9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('full_name', sa.String(length=255), nullable=True))
    op.add_column('order', sa.Column('phone_number', sa.String(length=15), nullable=True))
    op.create_unique_constraint(None, 'order', ['id'])
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'order', type_='unique')
    op.drop_column('order', 'phone_number')
    op.drop_column('order', 'full_name')
    # ### end Alembic commands ###
