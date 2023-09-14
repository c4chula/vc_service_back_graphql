import uuid
from typing import TYPE_CHECKING, List

import sqlalchemy
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vc_service_back.models import Base, DateTimeMixin

if TYPE_CHECKING:
    from vc_service_back.appointments.models import Appointment


class Employee(Base, DateTimeMixin):
    __tablename__ = "employees"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("uuid_generate_v4()"),
    )

    full_name: Mapped[str] = mapped_column(String(512), nullable=False)
    email: Mapped[str] = mapped_column(String(512), nullable=False, unique=True)
    phone_number: Mapped[str] = mapped_column(String(512), nullable=False, unique=True)
    employee_role_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("employee_roles.id"),
    )
    employee_role: Mapped["EmployeeRole"] = relationship(
        "EmployeeRole",
        back_populates="employees",
    )

    appointments: Mapped[List["Appointment"]] = relationship(
        back_populates="employee",
    )


class EmployeeRole(Base):
    __tablename__ = "employee_roles"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=sqlalchemy.text("uuid_generate_v4()"),
    )

    role_name: Mapped[str] = mapped_column(String(512), nullable=False, unique=True)
    employees: Mapped[List["Employee"]] = relationship(back_populates="employee_role")
