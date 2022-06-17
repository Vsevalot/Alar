"""init

Revision ID: c2ca2d7452fb
Revises: 
Create Date: 2022-06-16 11:17:50.690959

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'c2ca2d7452fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, autoincrement=True, nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=False, ),
        sa.Column('modified_at', sa.DateTime, nullable=True, ),
        sa.Column('deleted_at', sa.DateTime, nullable=True, ),
        sa.PrimaryKeyConstraint('id'),
        sa.Index('ix__users__names', 'name'),
        sa.UniqueConstraint('name', 'deleted_at')
    )

    op.create_table(
        'user_data',
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('hashed_password', sa.String, nullable=False),
        sa.ForeignKeyConstraint(('user_id', ), ('users.id', )),
        sa.UniqueConstraint('user_id')
    )

    op.create_table(
        'permissions',
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('permission', postgresql.ENUM('all', 'readonly', name='permission_enum')),
        sa.ForeignKeyConstraint(('user_id', ), ('users.id', )),
        sa.UniqueConstraint('user_id')
    )


def downgrade():
    op.drop_table('permissions')
    op.execute('DROP TYPE permission_enum;')
    op.drop_table('user_data')
    op.drop_table('users')
