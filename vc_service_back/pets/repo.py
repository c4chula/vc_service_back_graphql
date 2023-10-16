from typing import Sequence

from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from vc_service_back.models import EntityRepo
from vc_service_back.pets.models import Pet


class PetRepo(EntityRepo):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def get_all_pets(self, **filter) -> Sequence[Pet]:  # noqa: ANN003
        stmt = select(Pet)

        filter_set = [
            getattr(Pet, attr) == value
            for attr, value in filter.items()
            if hasattr(Pet, attr)
        ]

        if filter_set:
            stmt = stmt.filter(or_(*filter_set))

        result: Sequence[Pet] = (await self.session.execute(stmt)).scalars().fetchall()
        return result
