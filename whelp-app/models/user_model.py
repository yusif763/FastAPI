from enum import unique
import peewee
from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT
import os

from database import db

class User(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    username = peewee.CharField(unique=True,index=True)
    password = peewee.CharField()

    class Meta:
        database = db

class Settings(BaseModel):
    authjwt_secret_key: str = os.environ.get("SECRET_KEY","'dsjkadjkhadhkjadhjkadjkh4hj34234e2y8f989^^%&^$#^&*HAASDASD'")

@AuthJWT.load_config
def get_config():
    return Settings()