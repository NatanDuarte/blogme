import os

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from http import HTTPStatus
from api.model.post import Post
from api.config.database import get_database_collection
from dotenv import load_dotenv


load_dotenv()
app = FastAPI()

@app.get('/healthcheck')
def healthcheck():
    return {"status": "ok"}

@app.post('/posts')
def create_post(post: Post):
    try:
        collection = get_database_collection(
            database=os.getenv('DATABASE'),
            collection=os.getenv('POSTS_COLLECTION'),
        )

        post_id = collection.insert_one(post.dict()).inserted_id
        post_created = {"id": str(post_id), **post.dict()}
        return JSONResponse(content = post_created, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                            detail=f'Error inserting data: {str(e)}')
