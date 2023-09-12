import uuid
from datetime import timedelta
from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import DATERANGE, MONEY, TIMESTAMP, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vc_service_back.models import Base, DateTimeMixin

if TYPE_CHECKING:
    from vc_service_back.employee.models import Employee


class Appointment(Base, DateTimeMixin):
    __tablename__ = "appointments"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    employee_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("employees.id"))
    employee: Mapped["Employee"] = relationship()

    appointment_service_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("appointment_services.id"),
    )
    appointment_service: Mapped["AppointmentService"] = relationship(
        "AppointmentService",
        back_populates="appappointment_services",
    )

    appointment_comments: Mapped[List["AppointmentComment"]] = relationship(
        back_populates="appointments",
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
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(String(512), nullable=False, unique=True)
    duration: Mapped[timedelta] = mapped_column(DATERANGE, nullable=False)
    price: Mapped[MONEY] = mapped_column(MONEY)

    appointment: Mapped[List["Appointment"]] = relationship(
        back_populates="appointment_service",
    )


class AppointmentComment(Base, DateTimeMixin):
    __tablename__ = "appointment_comments"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    body: Mapped[str] = mapped_column(Text, nullable=False)

    appointment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("appointments.id"),
    )
    appointment: Mapped["Appointment"] = relationship(
        "Appointment",
        back_populates="appointments",
    )
