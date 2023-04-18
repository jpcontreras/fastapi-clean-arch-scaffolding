"""create users table

Revision ID: 0279a72914ba
Revises: 
Create Date: 2023-04-14 22:18:45.384100

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import func

from src.app.infrastructure.db.alembic_common import _add_timestamp_columns

# revision identifiers, used by Alembic.
revision = '0279a72914ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    table_name = 'users'
    op.create_table(
        table_name,
        sa.Column('id', sa.UUID, primary_key=True),
        sa.Column('provider', sa.Enum('facebook', 'google', 'email', name='providers'), nullable=False),
        sa.Column('uid', sa.String),
        sa.Column('email', sa.String),
        sa.Column('encrypted_password', sa.String),
        sa.Column('is_blocked', sa.Boolean, server_default=sa.sql.expression.false()),
    )
    _add_timestamp_columns(table_name)
    op.create_index('email_index', table_name, ['email'], unique=True)


def downgrade() -> None:
    op.drop_table('users')
