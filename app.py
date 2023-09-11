from fastapi import APIRouter, FastAPI

app = FastAPI()

main_router_v1 = APIRouter(
    prefix="/api/v1",
)

app.include_router(
    main_router_v1,
)
