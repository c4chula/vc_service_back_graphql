from typing import TYPE_CHECKING
from uuid import UUID

import strawberry
from strawberry.types import Info

from vc_service_back.employee.repo import EmployeeRoleRepo

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


@strawberry.type
class EmployeeRoleSchema:
    id: UUID
    role_name: str


@strawberry.type
class EmployeeSchema:
    id: UUID
    full_name: str
    email: str
    phone_number: str
    employee_role_id: strawberry.Private[UUID]

    async def get_employee_role(self, info: Info) -> EmployeeRoleSchema:
        session: AsyncSession = info.context["db_session"]
        employee_role = await EmployeeRoleRepo(session).get_employee_role_by_id(
            self.employee_role_id,
        )
        return EmployeeRoleSchema(
            id=employee_role.id,
            role_name=employee_role.role_name,
        )

    employee_role: EmployeeRoleSchema = strawberry.field(resolver=get_employee_role)
