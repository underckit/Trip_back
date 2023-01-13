from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import models
from config import  engine
from routers import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def start():
    return "ok"

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(crud.router)