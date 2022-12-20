from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.api.api_v1 import router
from app.models.user_model import User
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=F"{settings.API_V1_STR}/openapi.json"
)


@app.on_event("startup")
async def app_init():

    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).RESTfulTest

    await init_beanie(
        database=db_client,
        document_models=[
            User
        ]
    )

app.include_router(router.router, prefix=settings.API_V1_STR)
