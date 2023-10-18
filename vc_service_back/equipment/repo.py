from typing import Sequence
from uuid import UUID

from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from vc_service_back.equipment.models import Equipment
from vc_service_back.models import EntityRepo


class EquipmentRepo(EntityRepo):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def get_all_equipments(
        self,
        **filter,  # noqa: ANN003
    ) -> Sequence[Equipment]:
        stmt = select(Equipment)

        filter_set = [
            getattr(Equipment, attr) == value
            for attr, value in filter.items()
            if hasattr(Equipment, attr)
        ]

        if filter_set:
            stmt = stmt.filter(or_(*filter_set))

        result: Sequence[Equipment] = (
            (await self.session.execute(stmt)).scalars().fetchall()
        )
        return result

    async def get_equipment_by_id(self, id: UUID) -> Equipment:
        stmt = select(Equipment).where(Equipment.id == id)

        result: Equipment = (await self.session.execute(stmt)).scalar_one()
        return result
