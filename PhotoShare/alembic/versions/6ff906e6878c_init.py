"""Init

Revision ID: 6ff906e6878c
Revises: 2eab3ca08612
Create Date: 2023-10-11 17:07:23.824275

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ff906e6878c'
down_revision: Union[str, None] = '2eab3ca08612'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shares', sa.Column('crated_at', sa.DateTime(), nullable=True))
    op.add_column('shares', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shares', 'updated_at')
    op.drop_column('shares', 'crated_at')
    # ### end Alembic commands ###
