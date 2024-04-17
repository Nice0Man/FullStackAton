from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String, BigInteger, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import UserRelationMixin


class Token(Base, UserRelationMixin):
    _user_back_populates = "tokens"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    refresh_token: Mapped[UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    ua: Mapped[str] = mapped_column(String(200))
    ip: Mapped[str] = mapped_column(String(15), nullable=False)
    expires_in: Mapped[int] = mapped_column(BigInteger, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now()
    )
