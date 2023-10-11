from typing import TYPE_CHECKING, Sequence
from uuid import UUID

import strawberry
from strawberry.types import Info

from vc_service_back.employee.repo import EmployeeRepo, EmployeeRoleRepo
from vc_service_back.employee.schema import EmployeeRoleSchema, EmployeeSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


@strawberry.type
class EmployeeQuery:
    @strawberry.field
    async def all_employees(
        self,
        info: Info,
    ) -> Sequence[EmployeeSchema]:
        session: AsyncSession = info.context["db_session"]
        employees = await EmployeeRepo(session).get_all_employees()
        if employees is Exception:
            return []
        return [
            EmployeeSchema(
                id=data.id,
                full_name=data.full_name,
                email=data.email,
                phone_number=data.phone_number,
            )
            for data in employees
        ]


@strawberry.type
class EmployeeRoleQuery:
    @strawberry.field
    async def all_employee_roles(self, info: Info) -> Sequence[EmployeeRoleSchema]:
        session: AsyncSession = info.context["db_session"]
        employee_roles = await EmployeeRoleRepo(session).get_all_employee_roles()
        if employee_roles is Exception:
            return []
        return [
            EmployeeRoleSchema(
                id=data.id,
                role_name=data.role_name,
            )
            for data in employee_roles
        ]

    @strawberry.field
    async def get_employee_role_by_id(self, id: UUID, info: Info) -> EmployeeRoleSchema:
        session: AsyncSession = info.context["db_session"]
        employee_role = await EmployeeRoleRepo(session).get_employee_role_by_id(id)
        return EmployeeRoleSchema(
            id=employee_role.id,
            role_name=employee_role.role_name,
        )
