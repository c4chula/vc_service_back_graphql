from typing import TYPE_CHECKING, Sequence

import strawberry
from strawberry.types import Info

from vc_service_back.medications.repo import ManufacturerRepo, MedicationRepo
from vc_service_back.medications.schema import ManufacturerSchema, MedicationSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


@strawberry.type
class ManufacturerQuery:
    @strawberry.field
    async def all_manufactures(self, info: Info) -> Sequence[ManufacturerSchema]:
        session: AsyncSession = info.context["db_session"]
        manufactures = await ManufacturerRepo(session).get_all_manufactures()
        return [ManufacturerSchema(id=data.id, name=data.name) for data in manufactures]


@strawberry.type
class MedicationQuery:
    @strawberry.field
    async def all_medications(self, info: Info) -> Sequence[MedicationSchema]:
        session: AsyncSession = info.context["db_session"]
        medications = await MedicationRepo(session).get_all_medications()
        return [
            MedicationSchema(
                id=data.id,
                name=data.name,
                dosage=data.dosage,
                form=data.form,
                manufacturer_id=data.manufacturer_id,
            )
            for data in medications
        ]
