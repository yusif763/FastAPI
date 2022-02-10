from enum import unique
import peewee
from database import db


class Task(peewee.Model):
    task = peewee.CharField()


    class Meta:
        database = db
