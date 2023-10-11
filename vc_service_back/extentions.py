from strawberry.extensions import SchemaExtension
from strawberry.utils.await_maybe import AsyncIteratorOrIterator

from vc_service_back.database import get_async_session


class AsyncSessionExtention(SchemaExtension):
    async def on_operation(self) -> AsyncIteratorOrIterator[None]:
        async with await anext(get_async_session()) as session:
            self.execution_context.context["db_session"] = session
            yield
            self.execution_context.context["db_session"].close()
