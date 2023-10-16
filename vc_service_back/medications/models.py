import uuid
from typing import TYPE_CHECKING, List

import sqlalchemy
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vc_service_back.models import Base

if TYPE_CHECKING:
    from vc_service_back.appointments.models import Appointment


class Medication(Base):
    __tablename__ = "medications"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("uuid_generate_v4()"),
    )

    name: Mapped[str] = mapped_column(String(1024), nullable=False)
    dosage: Mapped[str] = mapped_column(String(1024), nullable=False)
    form: Mapped[str] = mapped_column(String(1024), nullable=False)

    manufacturer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("manufactures.id"),
        nullable=True,
    )

    manufacturer: Mapped["Manufacturer"] = relationship(
        "Manufacturer",
        back_populates="medications",
    )

    medication_records: Mapped[List["MedicationRecord"]] = relationship(
        back_populates="medication",
    )


class MedicationRecord(Base):
    __tablename__ = "medication_records"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("uuid_generate_v4()"),
    )

    appointment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("appointments.id"),
        nullable=True,
    )

    appointment: Mapped["Appointment"] = relationship(
        "Appointment",
        back_populates="medication_records",
    )

    medication_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("medications.id"),
        nullable=True,
    )
    medication: Mapped["Medication"] = relationship(
        "Medication",
        back_populates="medication_records",
    )


class Manufacturer(Base):
    __tablename__ = "manufactures"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("uuid_generate_v4()"),
    )

    name: Mapped[str] = mapped_column(String(1024), nullable=False)

    medications: Mapped[List["Medication"]] = relationship(
        back_populates="manufacturer",
    )
