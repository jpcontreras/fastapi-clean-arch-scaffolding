"""create user_profiles table

Revision ID: 8dc1a718c5c5
Revises: 0279a72914ba
Create Date: 2023-04-19 14:43:43.453251

"""
from alembic import op
import sqlalchemy as sa

from src.app.infrastructure.db.alembic_common import _add_timestamp_columns

# revision identifiers, used by Alembic.
revision = '8dc1a718c5c5'
down_revision = '0279a72914ba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    table_name = 'user_profiles'
    op.create_table(
        table_name,
        sa.Column('id', sa.UUID, primary_key=True),
        sa.Column('user_id', sa.UUID, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('first_name', sa.String, nullable=False),
        sa.Column('last_name', sa.String, nullable=False),
        sa.Column('alias_name', sa.String, nullable=True),
        sa.Column('image_url', sa.String, nullable=True)
    )
    _add_timestamp_columns(table_name)


def downgrade() -> None:
    op.drop_table('user_profiles')
