import uuid
from datetime import timedelta
from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, String, Text, text
from sqlalchemy.dialects.postgresql import DATERANGE, MONEY, TIMESTAMP, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vc_service_back.models import Base, DateTimeMixin

if TYPE_CHECKING:
    from vc_service_back.clients.models import Client
    from vc_service_back.employee.models import Employee
    from vc_service_back.equipment.models import EquipmentRecord
    from vc_service_back.medications.models import MedicationRecord
    from vc_service_back.pets.models import Pet


class Appointment(Base, DateTimeMixin):
    __tablename__ = "appointments"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
    )

    employee_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("employees.id"),
    )
    employee: Mapped["Employee"] = relationship(
        "Employee",
        back_populates="appointments",
    )

    client_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("clients.id"),
    )
    client: Mapped["Client"] = relationship("Client", back_populates="appointment")

    pet_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("pets.id"),
    )
    pet: Mapped["Pet"] = relationship(
        "Pet",
        back_populates="appointment",
    )

    appointment_service_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("appointment_services.id"),
    )
    appointment_service: Mapped["AppointmentService"] = relationship(
        "AppointmentService",
        back_populates="appappointments",
    )

    appointment_comments: Mapped[List["AppointmentComment"]] = relationship(
        back_populates="appointment",
    )

    medication_records: Mapped[List["MedicationRecord"]] = relationship(
        back_populates="appointment",
    )

    equipment_records: Mapped[List["EquipmentRecord"]] = relationship(
        back_populates="appointment",
    )

    appointment_date: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP,
        nullable=False,
    )


class AppointmentService(Base, DateTimeMixin):
    __tablename__ = "appointment_services"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
    )

    name: Mapped[str] = mapped_column(String(512), nullable=False, unique=True)
    duration: Mapped[timedelta] = mapped_column(DATERANGE, nullable=False)
    price: Mapped[MONEY] = mapped_column(MONEY)

    appointments: Mapped[List["Appointment"]] = relationship(
        back_populates="appointment_service",
    )


class AppointmentComment(Base, DateTimeMixin):
    __tablename__ = "appointment_comments"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("uuid_generate_v4()"),
    )

    body: Mapped[str] = mapped_column(Text, nullable=False)

    appointment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("appointments.id"),
    )
    appointment: Mapped["Appointment"] = relationship(
        "Appointment",
        back_populates="appointment_comments",
    )
