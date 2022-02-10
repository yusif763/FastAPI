import os
from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger
from ipdata import ipdata
from models.task_model import Task


RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_USERNAME = os.environ.get('RABBITMQ_USERNAME')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT')
PROD = os.environ.get('PROD')

celery = Celery(
    "whelp-app",  broker = f"amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:5672")


celery_log = get_task_logger(__name__)


IPDATA_API_KEY = os.environ.get(
    "API_KEY", "ddf3e15cb086965bb4cbfd984355ed97e47d951aec383d6c23e6f31e"
)
ipdata = ipdata.IPData(IPDATA_API_KEY)


@celery.task(name="create_new_task")
def create_new_task(ip):
    response = ipdata.lookup(ip)
    new_task = Task(task=response)
    new_task.save()
    celery_log.info(f"Task Complete!")
    return "Task Completed"
