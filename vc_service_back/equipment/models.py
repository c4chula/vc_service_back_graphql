import uuid
from typing import TYPE_CHECKING, List

import sqlalchemy
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vc_service_back.models import Base

if TYPE_CHECKING:
    from vc_service_back.appointments.models import Appointment


class Equipment(Base):
    __tablename__ = "equipments"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("uuid_generate_v4()"),
    )

    name: Mapped[str] = mapped_column(String(1024), nullable=False)
    model: Mapped[str] = mapped_column(String(1024), nullable=False)

    equipment_records: Mapped[List["EquipmentRecord"]] = relationship(
        back_populates="equipment",
    )


class EquipmentRecord(Base):
    __tablename__ = "equipment_records"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("uuid_generate_v4()"),
    )

    appointment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("appointments.id"),
    )

    appointment: Mapped["Appointment"] = relationship(
        "Appointment",
        back_populates="equipment_records",
    )

    equipment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("equipments.id"),
    )
    equipment: Mapped["Equipment"] = relationship(
        "Equipment",
        back_populates="equipment_records",
    )
