from collections.abc import Mapping
from datetime import UTC, datetime
from typing import Annotated, Any

from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, Query, status
from pymongo import ReturnDocument
from pymongo.asynchronous.collection import AsyncCollection

from config.database import get_comments_collection
from schema.schema import Comment, CommentCreate, CommentUpdate

v2_routes = APIRouter(prefix="/v2", tags=["API v2 routes"])


def _serialize_comment(document: Mapping[str, Any]) -> Comment:
    return Comment(id=str(document["_id"]), comment=document["comment"])


def _comment_id(comment_id: str) -> ObjectId:
    if not ObjectId.is_valid(comment_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Comment not found with id: {comment_id}",
        )
    return ObjectId(comment_id)


@v2_routes.get("/comments", name="Get all comments", response_model=list[Comment])
async def get_comments(
    collection: Annotated[
        AsyncCollection[dict[str, Any]], Depends(get_comments_collection)
    ],
    limit: Annotated[int, Query(ge=1, le=500)] = 100,
    offset: Annotated[int, Query(ge=0)] = 0,
) -> list[Comment]:
    documents = await (
        collection.find()
        .sort([("created_at", -1), ("_id", -1)])
        .skip(offset)
        .limit(limit)
        .to_list(length=limit)
    )
    return [_serialize_comment(document) for document in documents]


@v2_routes.get(
    "/comment/{comment_id}", name="Get comment by id", response_model=Comment
)
async def get_comment(
    comment_id: str,
    collection: Annotated[
        AsyncCollection[dict[str, Any]], Depends(get_comments_collection)
    ],
) -> Comment:
    document = await collection.find_one({"_id": _comment_id(comment_id)})
    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Comment not found with id: {comment_id}",
        )
    return _serialize_comment(document)


@v2_routes.post(
    "/create-comment",
    name="Create a new comment",
    response_model=Comment,
    status_code=status.HTTP_201_CREATED,
)
async def create_comment(
    comment: CommentCreate,
    collection: Annotated[
        AsyncCollection[dict[str, Any]], Depends(get_comments_collection)
    ],
) -> Comment:
    document = {"comment": comment.comment, "created_at": datetime.now(UTC)}
    result = await collection.insert_one(document)
    document["_id"] = result.inserted_id
    return _serialize_comment(document)


@v2_routes.put(
    "/update-comment/{comment_id}", name="Update comment by id", response_model=Comment
)
async def update_comment(
    comment_id: str,
    comment: CommentUpdate,
    collection: Annotated[
        AsyncCollection[dict[str, Any]], Depends(get_comments_collection)
    ],
) -> Comment:
    document = await collection.find_one_and_update(
        {"_id": _comment_id(comment_id)},
        {"$set": {"comment": comment.comment}},
        return_document=ReturnDocument.AFTER,
    )
    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Comment not found with id: {comment_id}",
        )
    return _serialize_comment(document)


@v2_routes.delete(
    "/delete-comment/{comment_id}", name="Delete comment by id", response_model=Comment
)
async def delete_comment(
    comment_id: str,
    collection: Annotated[
        AsyncCollection[dict[str, Any]], Depends(get_comments_collection)
    ],
) -> Comment:
    document = await collection.find_one_and_delete(
        {"_id": _comment_id(comment_id)}
    )
    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Comment not found with id: {comment_id}",
        )
    return _serialize_comment(document)
