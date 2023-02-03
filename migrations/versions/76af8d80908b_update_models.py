"""update models

Revision ID: 76af8d80908b
Revises: 403abbf5418a
Create Date: 2023-02-02 20:53:05.610314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76af8d80908b'
down_revision = '403abbf5418a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'phone_number')
    op.drop_column('customer', 'password')
    op.drop_column('customer', 'user_name')
    op.add_column('item', sa.Column('bottle', sa.String(), nullable=True))
    op.add_column('item', sa.Column('flavor', sa.String(), nullable=True))
    op.add_column('item', sa.Column('quantity', sa.Integer(), nullable=True))
    op.add_column('item', sa.Column('spirit', sa.String(), nullable=True))
    op.drop_column('item', 'spirit_flavor')
    op.drop_column('item', 'age_time')
    op.drop_column('item', 'bottle_type')
    op.drop_column('item', 'spirit_type')
    op.drop_column('item', 'bottle_quantity')
    op.add_column('label', sa.Column('message_font', sa.String(), nullable=True))
    op.add_column('label', sa.Column('name_font', sa.String(), nullable=True))
    op.drop_column('label', 'font')
    op.drop_column('order', 'sub_total')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('sub_total', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('label', sa.Column('font', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('label', 'name_font')
    op.drop_column('label', 'message_font')
    op.add_column('item', sa.Column('bottle_quantity', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('item', sa.Column('spirit_type', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('item', sa.Column('bottle_type', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('item', sa.Column('age_time', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('item', sa.Column('spirit_flavor', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('item', 'spirit')
    op.drop_column('item', 'quantity')
    op.drop_column('item', 'flavor')
    op.drop_column('item', 'bottle')
    op.add_column('customer', sa.Column('user_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('customer', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('customer', sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
