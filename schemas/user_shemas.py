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



class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserLoginResponseSchema(BaseModel):
    user: str
    access_token: str
    refresh_token: str


class User(UserBase):
    id: int
    username: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
