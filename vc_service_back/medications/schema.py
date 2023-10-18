from typing import TYPE_CHECKING, List
from uuid import UUID

import strawberry
from strawberry.types import Info

from vc_service_back.medications.repo import ManufacturerRepo, MedicationRepo

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


@strawberry.type
class MedicationSchema:
    id: UUID
    name: str
    dosage: str
    form: str

    manufacturer_id: strawberry.Private[UUID]

    @strawberry.field
    async def manufacturer(self, info: Info) -> "ManufacturerSchema":
        session: AsyncSession = info.context["db_session"]
        data = await ManufacturerRepo(session).get_manufacturer_by_id(
            self.manufacturer_id,
        )
        return ManufacturerSchema(id=data.id, name=data.name)


@strawberry.type
class ManufacturerSchema:
    id: UUID
    name: str

    @strawberry.field
    async def medications(self, info: Info) -> List[MedicationSchema]:
        session: AsyncSession = info.context["db_session"]
        medications = await MedicationRepo(session).get_all_medications(
            manufacturer_id=self.id,
        )
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
