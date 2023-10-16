from abc import ABC, abstractmethod
from typing import Sequence
from uuid import UUID

from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from vc_service_back.employee.models import Employee, EmployeeRole


class EntityRepo(ABC):
    @abstractmethod
    def __init__(self, session: AsyncSession) -> None:
        self.session = session


class EmployeeRepo(EntityRepo):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def get_all_employees(self, **filter) -> Sequence[Employee]:  # noqa: ANN003
        stmt = select(Employee)

        filter_set = [
            getattr(Employee, attr) == value
            for attr, value in filter.items()
            if hasattr(Employee, attr)
        ]

        if filter_set:
            stmt = stmt.filter(or_(*filter_set))

        result: Sequence[Employee] = (
            (await self.session.execute(stmt)).scalars().fetchall()
        )
        return result


class EmployeeRoleRepo(EntityRepo):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def get_all_employee_roles(self) -> Sequence[EmployeeRole]:
        stmt = select(EmployeeRole)
        result = await self.session.execute(stmt)
        return result.scalars().fetchall()

    async def get_employee_role_by_id(self, id: UUID) -> EmployeeRole:
        stmt = select(EmployeeRole).where(EmployeeRole.id == id)
        result = await self.session.execute(stmt)
        return result.scalar_one()
