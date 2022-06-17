from sqlalchemy import (
    MetaData,
    Column,
    DateTime,
    Integer,
    Table,
    String,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import ENUM


metadata = MetaData()

user_table = Table(
    'users',
    metadata,
    Column('id', Integer, nullable=False, primary_key=True),
    Column('name', String, index=True, nullable=False),
    Column('created_at', DateTime, nullable=False,),
    Column('modified_at', DateTime, nullable=True,),
    Column('deleted_at', DateTime, nullable=True,),
    UniqueConstraint('name', 'deleted_at'),
)

user_data_table = Table(
    'user_data',
    metadata,
    Column('user_id', Integer, ForeignKey(user_table.c.id), unique=True),
    Column('hashed_password', String),
)

permission_enum = ENUM(
    ('all', 'readonly'),
    name='permission_enum',
    metadata=metadata,
)

permission_table = Table(
    'permissions',
    metadata,
    Column('user_id', Integer, ForeignKey(user_table.c.id)),
    Column('permission', permission_enum),
    UniqueConstraint('user_id', 'permission')
)
