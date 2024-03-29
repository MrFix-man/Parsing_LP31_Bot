"""Initial

Revision ID: 43d0e33c08a4
Revises: 
Create Date: 2024-01-28 15:10:13.840079

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '43d0e33c08a4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pars_avito',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('avito_id', sa.BigInteger(), nullable=True),
                    sa.Column('rooms', sa.String(length=50), nullable=True),
                    sa.Column('area', sa.Float(precision=9), nullable=True),
                    sa.Column('price', sa.String(length=20), nullable=True),
                    sa.Column('adress', sa.String(length=150), nullable=True),
                    sa.Column('district', sa.String(), nullable=True),
                    sa.Column('floor_level', sa.String(), nullable=True),
                    sa.Column('url_offer', sa.String(), nullable=True),
                    sa.Column('type', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('avito_id'),
                    )

    op.create_table('pars_drom',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('price_int', sa.BigInteger(), nullable=True),
                    sa.Column('day_of_announcement', sa.String(length=10), nullable=True),
                    sa.Column('type', sa.String(length=50), nullable=True),
                    sa.Column('town', sa.String(length=50), nullable=True),
                    sa.Column('short_descript', sa.String(), nullable=True),
                    sa.Column('car_year', sa.String(), nullable=True),
                    sa.Column('car_name', sa.String(), nullable=True),
                    sa.Column('url_cars', sa.String(), nullable=True),
                    sa.Column('site_evaluation', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('url_cars')
                    )




# ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pars_drom')
    op.drop_table('pars_avito')
    # ### end Alembic commands ###
