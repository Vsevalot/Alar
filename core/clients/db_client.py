from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from sqlalchemy.dialects.postgresql import insert
from core.db.schema import user_table, permission_table, user_data_table


SELECT_USER_QUERY = """
    SELECT u.id, u.name, p.permission 
    FROM users u 
    JOIN permissions p ON u.id = p.user_id 
    WHERE u.deleted_at IS NULL
"""

ORDER_BY_CREATED = "ORDER BY u.created_at"


"""
It's better to keep the same approach everywhere. 
But the task was to use both ORM and raw SQL.
"""
class DBClient:
    def __init__(self, db_dsn: str):
        engine = create_async_engine(db_dsn, future=True, echo=True)
        self.session = sessionmaker(
            engine,
            expire_on_commit=False,
            class_=AsyncSession,
        )

    async def get_users(self):
        async with self.session() as session:
            async with session.begin():
                query = sqlalchemy.text(f'{SELECT_USER_QUERY}'
                                        f'{ORDER_BY_CREATED}')
                q = await session.execute(query)
                return q.all()

    async def get_user(self, user_id: int):
        async with self.session() as session:
            async with session.begin():
                query = sqlalchemy.text(
                    f'{SELECT_USER_QUERY} AND u.id = {user_id}'
                )
                result = await session.execute(query)
                return dict(result.fetchone())

    async def create_user(self, name: str):
        async with self.session() as session:
            async with session.begin():
                stmt = insert(user_table).values(
                    name=name,
                )
                result = await session.execute(stmt)
                session.commit()
                return {'id': result.inserted_primary_key[0], 'name': name}

    async def update_user(self, id: int, name: str):
        async with self.session() as session:
            async with session.begin():
                stmt = sqlalchemy.update(user_table).values(
                    name=name,
                ).where(user_table.c.id == id)
                await session.execute(stmt)
                session.commit()
                return {'id': id, 'name': name}


    async def create_password(
            self,
            user_id: int,
            hashed_password: str,
    ):
        async with self.session() as session:
            async with session.begin():
                stmt = insert(user_data_table).values(
                    user_id=user_id,
                    hashed_password=hashed_password,
                )
                await session.execute(stmt)
                session.commit()

    async def update_password(
            self,
            user_id: int,
            hashed_password: str,
    ):
        async with self.session() as session:
            async with session.begin():
                stmt = sqlalchemy.update(user_data_table).values(
                    hashed_password=hashed_password,
                ).where(user_data_table.c.user_id == user_id)
                await session.execute(stmt)
                session.commit()

    async def create_permission(
            self,
            user_id: int,
            permission: str,
    ):
        async with self.session() as session:
            async with session.begin():
                stmt = insert(permission_table).values(
                    user_id=user_id,
                    permission=permission,
                )
                await session.execute(stmt)
                session.commit()

    async def update_permission(
            self,
            user_id: int,
            permission: str,
    ):
        async with self.session() as session:
            async with session.begin():
                stmt = sqlalchemy.update(permission_table).values(
                    permission=permission,
                ).where(permission_table.c.user_id == user_id)
                await session.execute(stmt)
                session.commit()

    async def soft_delete_user(self, user_id: int):
        async with self.session() as session:
            async with session.begin():
                stmt = sqlalchemy.update(user_table).values(
                    deleted_at=sqlalchemy.func.now(),
                ).where(user_table.c.id == user_id)
                await session.execute(stmt)
                session.commit()
