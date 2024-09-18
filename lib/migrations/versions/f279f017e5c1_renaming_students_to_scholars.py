"""Renaming students to scholars

Revision ID: f279f017e5c1
Revises: 791279dd0760
Create Date: 2024-09-18 12:18:52.321966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f279f017e5c1'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
