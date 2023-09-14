import uuid
from typing import TYPE_CHECKING, List

import sqlalchemy
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vc_service_back.models import Base, DateTimeMixin

if TYPE_CHECKING:
    from vc_service_back.appointments.models import Appointment
    from vc_service_back.pets.models import PetOwnerAssociation


class Client(Base, DateTimeMixin):
    __tablename__ = "clients"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("uuid_generate_v4()"),
    )

    full_name: Mapped[str] = mapped_column(String(512), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(512), nullable=False)
    email: Mapped[str] = mapped_column(String(512), nullable=True)

    appointment: Mapped[List["Appointment"]] = relationship(
        back_populates="client",
    )

    pets: Mapped[List["PetOwnerAssociation"]] = relationship(back_populates="owner")
