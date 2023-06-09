"""Initial migration

Revision ID: 94eba7183e46
Revises: 
Create Date: 2023-05-08 22:46:25.020772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94eba7183e46'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hotels',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('location', sa.String(), nullable=False),
        sa.Column('services', sa.JSON(), nullable=True),
        sa.Column('room_quantity', sa.Integer(), nullable=False),
        sa.Column('image_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('playground')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('playground',
    sa.Column('equip_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('type', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('color', sa.VARCHAR(length=25), autoincrement=False, nullable=False),
    sa.Column('location', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('install_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.CheckConstraint("location::text = ANY (ARRAY['north'::character varying, 'south'::character varying, 'west'::character varying, 'east'::character varying, 'northeast'::character varying, 'southeast'::character varying, 'southwest'::character varying, 'northwest'::character varying]::text[])", name='playground_location_check'),
    sa.PrimaryKeyConstraint('equip_id', name='playground_pkey')
    )
    op.drop_table('hotels')
    # ### end Alembic commands ###
