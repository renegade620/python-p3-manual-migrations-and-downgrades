"""Renaming email to email_address

Revision ID: 6e0614c804d2
Revises: f279f017e5c1
Create Date: 2024-09-18 13:13:11.571546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e0614c804d2'
down_revision = 'f279f017e5c1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'email', new_column_name='email_address')



def downgrade() -> None:
    op.alter_column('students', 'email_address', new_column_name='email')

