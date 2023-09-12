from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


class DateTimeMixin:
    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        server_onupdate=func.current_timestamp(),
    )
