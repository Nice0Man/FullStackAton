import uuid

from sqlalchemy import Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True
    _table_uuid: bool = False

    @declared_attr
    def __tablename__(self) -> str:
        return f"{self.__name__.lower()}s"

    @declared_attr.directive
    def id(self):
        if not self._table_uuid:
            return mapped_column(
                Integer, primary_key=True, autoincrement=True, nullable=False
            )
        return mapped_column(
            UUID(as_uuid=True),
            primary_key=True,
            default=uuid.uuid4,
            unique=True,
            nullable=False,
        )
