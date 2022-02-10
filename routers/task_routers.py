from email import message
import json
import requests
from main import app
from models.user_model import User
import schemas.task_schemas as task_schemas
from fastapi import APIRouter,Request
from celery_app.worker import create_new_task
from models.task_model import Task
import socket


router = APIRouter()

@router.post("/task",status_code=201)
async def create_tasks(request: Request):
    ip = requests.get('http://ipinfo.io/json').json()['ip']
    task = create_new_task.delay(ip)
    return "Task Completed"


@router.post("/status/{task_id}")
def get_task(task_id):
    task = Task.filter(id = task_id).first()
    return {"task":task.__data__}