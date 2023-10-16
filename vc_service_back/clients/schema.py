from uuid import UUID

import strawberry


@strawberry.type
class ClientSchema:
    id: UUID
