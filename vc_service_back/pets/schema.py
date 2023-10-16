from datetime import datetime
from uuid import UUID

import strawberry


@strawberry.type
class PetSchema:
    id: UUID
    name: str
    species: str
    breed: str

    date_of_birth: datetime
