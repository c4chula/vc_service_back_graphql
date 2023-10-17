from uuid import UUID

import strawberry


@strawberry.type
class ManufacturerSchema:
    id: UUID
    name: str
