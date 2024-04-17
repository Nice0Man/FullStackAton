from typing import TYPE_CHECKING
from uuid import UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .users import User


class UserRelationMixin:
    _user_id_unique: bool = False
    _user_back_populates: str | None = None
    _user_id_nullable: bool = False

    user_id: Mapped[UUID]

    @declared_attr
    def user_id(self) -> Mapped[UUID]:
        return mapped_column(
            ForeignKey("users.id"),
            unique=self._user_id_unique,
            nullable=self._user_id_nullable,
        )

    @declared_attr
    def user(self) -> Mapped["User"]:
        return relationship("User", back_populates=self._user_back_populates)
