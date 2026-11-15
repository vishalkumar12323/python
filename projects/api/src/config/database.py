from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, Request
from pymongo import AsyncMongoClient
from pymongo.asynchronous.collection import AsyncCollection

from config.settings import settings

COMMENTS_COLLECTION = "comments"


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    client: AsyncMongoClient[dict[str, Any]] = AsyncMongoClient(
        settings.mongodb_uri,
        serverSelectionTimeoutMS=settings.mongodb_server_selection_timeout_ms,
    )
    try:
        await client.admin.command("ping")
        database = client[settings.mongodb_database]
        collection = database[COMMENTS_COLLECTION]
        await collection.create_index([("created_at", -1), ("_id", -1)])
        app.state.comments_collection = collection
        yield
    finally:
        await client.close()


def get_comments_collection(
    request: Request,
) -> AsyncCollection[dict[str, Any]]:
    return request.app.state.comments_collection