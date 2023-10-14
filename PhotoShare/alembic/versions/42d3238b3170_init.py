"""Init

Revision ID: 42d3238b3170
Revises: 360758615c6e
Create Date: 2023-10-14 09:09:34.734339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42d3238b3170'
down_revision: Union[str, None] = '360758615c6e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('users_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['users_id'], ['id'], ondelete='CASCADE')
    op.add_column('shares', sa.Column('url', sa.String(), nullable=False))
    op.add_column('shares', sa.Column('image_qr', sa.String(), nullable=True))
    op.drop_index('ix_shares_image', table_name='shares')
    op.drop_index('ix_shares_name_share', table_name='shares')
    op.drop_index('ix_shares_qrcode', table_name='shares')
    op.create_index(op.f('ix_shares_image_qr'), 'shares', ['image_qr'], unique=False)
    op.create_index(op.f('ix_shares_url'), 'shares', ['url'], unique=False)
    op.drop_column('shares', 'qrcode')
    op.drop_column('shares', 'name_share')
    op.drop_column('shares', 'image')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shares', sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('shares', sa.Column('name_share', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('shares', sa.Column('qrcode', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_shares_url'), table_name='shares')
    op.drop_index(op.f('ix_shares_image_qr'), table_name='shares')
    op.create_index('ix_shares_qrcode', 'shares', ['qrcode'], unique=False)
    op.create_index('ix_shares_name_share', 'shares', ['name_share'], unique=False)
    op.create_index('ix_shares_image', 'shares', ['image'], unique=False)
    op.drop_column('shares', 'image_qr')
    op.drop_column('shares', 'url')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'users_id')
    # ### end Alembic commands ###
