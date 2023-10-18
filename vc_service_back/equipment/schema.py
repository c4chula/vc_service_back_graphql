from uuid import UUID

import strawberry


@strawberry.type
class EquipmentSchema:
    id: UUID
    name: str
    model: str
