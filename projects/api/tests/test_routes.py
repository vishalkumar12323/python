import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock

from bson import ObjectId
from fastapi import HTTPException
from pymongo import ReturnDocument

from api.v1.route import create_comment, delete_comment, get_comment, update_comment
from schema.schema import CommentCreate, CommentUpdate


class CommentRouteTests(unittest.IsolatedAsyncioTestCase):
    async def test_create_comment_persists_and_returns_generated_id(self) -> None:
        comment_id = ObjectId()
        collection = MagicMock()
        collection.insert_one = AsyncMock(
            return_value=SimpleNamespace(inserted_id=comment_id)
        )

        result = await create_comment(
            CommentCreate(comment="A comment"),
            collection,
        )

        collection.insert_one.assert_awaited_once()
        stored_document = collection.insert_one.await_args.args[0]
        self.assertEqual(stored_document["comment"], "A comment")
        self.assertIn("created_at", stored_document)
        self.assertEqual(result.id, str(comment_id))
        self.assertEqual(result.comment, "A comment")

    async def test_get_comment_returns_persisted_document(self) -> None:
        comment_id = ObjectId()
        collection = MagicMock()
        collection.find_one = AsyncMock(
            return_value={"_id": comment_id, "comment": "Stored"}
        )

        result = await get_comment(str(comment_id), collection)

        collection.find_one.assert_awaited_once_with({"_id": comment_id})
        self.assertEqual(result.id, str(comment_id))
        self.assertEqual(result.comment, "Stored")

    async def test_update_comment_uses_atomic_update(self) -> None:
        comment_id = ObjectId()
        collection = MagicMock()
        collection.find_one_and_update = AsyncMock(
            return_value={"_id": comment_id, "comment": "Updated"}
        )

        result = await update_comment(
            str(comment_id),
            CommentUpdate(comment="Updated"),
            collection,
        )

        collection.find_one_and_update.assert_awaited_once_with(
            {"_id": comment_id},
            {"$set": {"comment": "Updated"}},
            return_document=ReturnDocument.AFTER,
        )
        self.assertEqual(result.comment, "Updated")

    async def test_invalid_comment_id_returns_not_found(self) -> None:
        collection = MagicMock()
        collection.find_one = AsyncMock()

        with self.assertRaises(HTTPException) as error:
            await get_comment("invalid-id", collection)

        self.assertEqual(error.exception.status_code, 404)
        collection.find_one.assert_not_awaited()

    async def test_delete_missing_comment_returns_not_found(self) -> None:
        collection = MagicMock()
        collection.find_one_and_delete = AsyncMock(return_value=None)

        with self.assertRaises(HTTPException) as error:
            await delete_comment(str(ObjectId()), collection)

        self.assertEqual(error.exception.status_code, 404)


if __name__ == "__main__":
    unittest.main()
