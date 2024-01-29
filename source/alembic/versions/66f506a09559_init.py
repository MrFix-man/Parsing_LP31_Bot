"""Init

Revision ID: 66f506a09559
Revises: 43d0e33c08a4
Create Date: 2024-01-28 19:11:02.074402

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66f506a09559'
down_revision: Union[str, None] = '43d0e33c08a4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
