from typing import TYPE_CHECKING, Sequence

import strawberry
from strawberry.types import Info

from vc_service_back.equipment.repo import EquipmentRepo
from vc_service_back.equipment.schema import EquipmentSchema

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


@strawberry.type
class EquipmentQuery:
    @strawberry.field
    async def all_equipment(self, info: Info) -> Sequence[EquipmentSchema]:
        session: AsyncSession = info.context["db_session"]
        manufactures = await EquipmentRepo(session).get_all_equipments()
        return [
            EquipmentSchema(id=data.id, name=data.name, model=data.model)
            for data in manufactures
        ]
