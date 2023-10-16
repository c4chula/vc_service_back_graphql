import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from strawberry.tools import merge_types

from vc_service_back.employee.query import EmployeeQuery, EmployeeRoleQuery
from vc_service_back.extentions import AsyncSessionExtention
from vc_service_back.pets.query import PetQuery

app = FastAPI()

merged_query = merge_types(
    name="Query",
    types=(EmployeeQuery, EmployeeRoleQuery, PetQuery),
)

schema = strawberry.Schema(merged_query, extensions=[AsyncSessionExtention])
graphql_app = GraphQL(schema)

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
