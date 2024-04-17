from asyncio import current_task
from typing import Any

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)

from backend.src.api.core.config import settings


class DataBaseManage:
    def __init__(self, url: str, echo: bool) -> None:
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )

    def get_scoped_session(self) -> AsyncSession | Any:
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(self) -> AsyncSession:
        sess = self.get_scoped_session()
        try:
            yield sess
        except Exception as ex:
            print(ex)
        finally:
            await sess.close()


db_manage = DataBaseManage(url=settings.db.db_url, echo=settings.db.db_echo)
