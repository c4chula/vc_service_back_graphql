import uuid
from datetime import datetime
from typing import TYPE_CHECKING, List

import sqlalchemy
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vc_service_back.models import Base, DateTimeMixin

if TYPE_CHECKING:
    from vc_service_back.appointments.models import Appointment
    from vc_service_back.clients.models import Client


class Pet(Base, DateTimeMixin):
    __tablename__ = "pets"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("uuid_generate_v4()"),
    )

    name: Mapped[str] = mapped_column(String(512), nullable=False)
    species: Mapped[str] = mapped_column(String(512), nullable=False)
    breed: Mapped[str] = mapped_column(String(1024), nullable=True)

    date_of_birth: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)

    owners: Mapped[List["Client"]] = relationship(back_populates="pet")

    appointment: Mapped["Appointment"] = relationship(
        back_populates="pet",
    )
