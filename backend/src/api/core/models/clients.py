from datetime import datetime
from sqlalchemy import String, DateTime

from .base import Base, Mapped, mapped_column

from enum import Enum

from .mixins import UserRelationMixin


class ClientStatus(str, Enum):
    NOT_AT_WORK = "Не в работе"
    IN_PROGRESS = "В работе"
    REJECTED = "Отказ"
    CLOSED = "Сделка закрыта"


class Client(UserRelationMixin, Base):
    _table_uuid = True
    _back_populates = "clients"

    name: Mapped[str] = mapped_column(String(32), nullable=False)
    surname: Mapped[str] = mapped_column(String(32), nullable=False)
    birthday: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    TIN: Mapped[str] = mapped_column(String(12), nullable=False, unique=True)
    responsible_person_full_name: Mapped[str] = mapped_column(unique=True)
    status: Mapped[str] = mapped_column(
        nullable=False,
        default=ClientStatus.NOT_AT_WORK,
        server_default=ClientStatus.NOT_AT_WORK,
    )
