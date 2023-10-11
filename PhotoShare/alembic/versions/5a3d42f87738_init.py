"""Init

Revision ID: 5a3d42f87738
Revises: 
Create Date: 2023-10-11 16:17:09.850051

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a3d42f87738'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(length=25), nullable=False),
    sa.Column('crated_at', sa.DateTime(), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_role'), 'users', ['role'], unique=False)
    op.create_table('shares',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_share', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('qrcode', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_shares_description'), 'shares', ['description'], unique=False)
    op.create_index(op.f('ix_shares_id'), 'shares', ['id'], unique=False)
    op.create_index(op.f('ix_shares_image'), 'shares', ['image'], unique=False)
    op.create_index(op.f('ix_shares_name_share'), 'shares', ['name_share'], unique=True)
    op.create_index(op.f('ix_shares_qrcode'), 'shares', ['qrcode'], unique=False)
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('crated_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('shares_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['shares_id'], ['shares.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_id'), 'comments', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_id'), table_name='comments')
    op.drop_table('comments')
    op.drop_index(op.f('ix_shares_qrcode'), table_name='shares')
    op.drop_index(op.f('ix_shares_name_share'), table_name='shares')
    op.drop_index(op.f('ix_shares_image'), table_name='shares')
    op.drop_index(op.f('ix_shares_id'), table_name='shares')
    op.drop_index(op.f('ix_shares_description'), table_name='shares')
    op.drop_table('shares')
    op.drop_index(op.f('ix_users_role'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
