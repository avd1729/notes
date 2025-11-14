"""Add password column to users

Revision ID: 074b478b90cc
Revises: 
Create Date: 2025-11-14 15:04:37.241987

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers
revision = 'xxxx'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "users",
        sa.Column("password", sa.String(length=255), nullable=False, server_default="temp_default")
    )

def downgrade():
    op.drop_column("users", "password")

