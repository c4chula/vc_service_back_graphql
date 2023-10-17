from typing import Sequence

from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from vc_service_back.medications.models import Manufacturer
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
