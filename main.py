from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] =None ):
    if published:
        return {'data': f'{limit} blog from db. {sort}'}
    else:
        return {'data': 'All blogs from db.'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data' : 'all unplublished blog'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comment')
def comments(id: int, limit=10):
    return {'data' : f'{id} and {limit}'}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'blog is created with {request.title}'}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)