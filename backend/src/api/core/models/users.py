from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship

from .base import Base, Mapped, mapped_column

if TYPE_CHECKING:
    from .clients import Client


class User(Base):
    _table_uuid = True

    full_name: Mapped[str] = mapped_column(nullable=False, unique=True)
    login: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[bytes] = mapped_column(nullable=False)
    clients: Mapped[list["Client"]] = relationship(back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.full_name!r})"

    def __repr__(self):
        return str(self)
