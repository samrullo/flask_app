"""empty message

Revision ID: 35d0070d4e46
Revises: 
Create Date: 2022-02-18 16:01:49.086510

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '35d0070d4e46'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('base_model')
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('modified_at', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.drop_column('users', 'phone')
    op.drop_column('users', 'profile')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'modified_at')
    op.drop_column('users', 'created_at')
    op.create_table('base_model',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('modified_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='base_model_pkey')
    )
    # ### end Alembic commands ###