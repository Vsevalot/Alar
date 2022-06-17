"""first_user

Revision ID: 0a071b987c7d
Revises: c2ca2d7452fb
Create Date: 2022-06-16 11:50:19.270167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a071b987c7d'
down_revision = 'c2ca2d7452fb'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("INSERT INTO users (id, name) VALUES (0, 'admin')")
    op.execute("INSERT INTO user_data (user_id, hashed_password) "
               "VALUES (0, 'e4315063c76f03cf6379dd8e4373c0dd3ffe5792b1a57983c3bfd4bb9cabc9ed')")
    op.execute("INSERT INTO permissions (user_id, permission) VALUES (0, 'all')")

def downgrade():
    op.execute("DELETE FROM permissions WHERE permissions.user_id = 0")
    op.execute("DELETE FROM user_data WHERE user_data.user_id = 0")
    op.execute("DELETE FROM users WHERE users.id = 0")
