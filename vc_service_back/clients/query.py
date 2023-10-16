import strawberry


@strawberry.type
class ClientQuery:
    @strawberry.field
    async def get_all_clients() -> None:
        ...
