from typing import Sequence
from uuid import UUID

from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from vc_service_back.medications.models import Manufacturer, Medication
from vc_service_back.models import EntityRepo


class ManufacturerRepo(EntityRepo):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def get_all_manufactures(
        self,
        **filter,  # noqa: ANN003
    ) -> Sequence[Manufacturer]:
        stmt = select(Manufacturer)

        filter_set = [
            getattr(Manufacturer, attr) == value
            for attr, value in filter.items()
            if hasattr(Manufacturer, attr)
        ]

        if filter_set:
            stmt = stmt.filter(or_(*filter_set))

        result: Sequence[Manufacturer] = (
            (await self.session.execute(stmt)).scalars().fetchall()
        )
        return result

    async def get_manufacturer_by_id(self, id: UUID) -> Manufacturer:
        stmt = select(Manufacturer).where(Manufacturer.id == id)

        result: Manufacturer = (await self.session.execute(stmt)).scalar_one()
        return result


class MedicationRepo(EntityRepo):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def get_all_medications(
        self,
        **filter,  # noqa: ANN003
    ) -> Sequence[Medication]:
        stmt = select(Medication)

        filter_set = [
            getattr(Manufacturer, attr) == value
            for attr, value in filter.items()
            if hasattr(Manufacturer, attr)
        ]

        if filter_set:
            stmt = stmt.filter(or_(*filter_set))

        result: Sequence[Medication] = (
            (await self.session.execute(stmt)).scalars().fetchall()
        )
        return result
