from asyncio import tasks
from typing import List
from database import db
from fastapi import Depends, FastAPI
from models.user_model import User
from models.task_model import Task


db.connect()
db.create_tables([User,Task])
db.close()

app = FastAPI()

# from routers.routers import create_user
from routers import user_routers
from routers import task_routers


app.include_router(
    task_routers.router,prefix="/api/v1"
)
app.include_router(
    user_routers.router,prefix="/api/v1"
)
