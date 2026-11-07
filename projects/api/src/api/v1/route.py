from fastapi import APIRouter

v1_routes = APIRouter(prefix="/v1", tags=["API v1 routes"])

@v1_routes.get("/comments", name="Get all comments")
def get_comments():
    pass

@v1_routes.get("/comment/{comment_id}", name="Get comment by id")
def get_comment(comment_id: str):
    pass

@v1_routes.post("/create-comment", name="Create a new comment")
def create_comment(comment: dict):
    pass

@v1_routes.patch("/update-comment/{comment_id}", name="Update comment by id")
def update_comment(comment_id: str):
    pass

@v1_routes.delete("/delete-comment/{comment_id}", name="Delete comment by id")
def delete_comment(comment_id: str):
    pass