from typing import TYPE_CHECKING, Sequence

import strawberry
from strawberry.types import Info

from vc_service_back.pets.repo import PetRepo
from vc_service_back.pets.schema import PetSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


@strawberry.type
class PetQuery:
    @strawberry.field
    async def all_pets(self, info: Info) -> Sequence[PetSchema]:
        session: AsyncSession = info.context["db_session"]
        pets = await PetRepo(session).get_all_pets()
        return [
            PetSchema(
                id=data.id,
                name=data.name,
                species=data.species,
                breed=data.breed,
                date_of_birth=data.date_of_birth,
            )
            for data in pets
        ]
