import uuid

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vc_service_back.models import Base


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    full_name: Mapped[str] = mapped_column(String(512), nullable=False)
    email: Mapped[str] = mapped_column(String(512), nullable=False, unique=True)
    phone_number: Mapped[str] = mapped_column(String(512), nullable=False, unique=True)
    employee_role_id: Mapped[UUID] = mapped_column(ForeignKey("employee_roles.id"))
    empolyee_role: Mapped["EmployeeRole"] = relationship()


class EmployeeRole(Base):
    __tablename__ = "employee_roles"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    role_name: Mapped[str] = mapped_column(String(512), nullable=False, unique=True)
