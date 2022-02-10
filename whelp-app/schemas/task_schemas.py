from typing import Any, List, Optional

import peewee
from pydantic import BaseModel, Json
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res



class TaskBase(BaseModel):
    task: str


class TaskCreate(TaskBase):
    task: str

class GetTask(BaseModel):
    id:int


# class TaskResponseSchema(BaseModel):
#     task_id: int


class Task(TaskBase):
    id: int
    task: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
