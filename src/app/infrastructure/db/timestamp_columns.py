from alembic import op
import sqlalchemy as sa


def _add_timestamp_columns(table_name):
    op.add_column(table_name, sa.Column('created_at', sa.DateTime(), nullable=False,
                                        server_default=sa.text("(now() at time zone 'utc')")))
    op.add_column(table_name, sa.Column('updated_at', sa.DateTime(), nullable=False,
                                        server_default=sa.text("(now() at time zone 'utc')")))
