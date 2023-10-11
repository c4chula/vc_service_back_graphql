from strawberry.extensions import SchemaExtension
from strawberry.utils.await_maybe import AsyncIteratorOrIterator

from vc_service_back.database import async_session_maker


class AsyncSessionExtention(SchemaExtension):
    async def on_operation(self) -> AsyncIteratorOrIterator[None]:
        async with async_session_maker() as session:
            self.execution_context.context["db_session"] = session
            yield
            del self.execution_context.context["db_session"]
