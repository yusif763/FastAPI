FROM python:3.8



COPY ./requirements.txt /usr/src/

RUN pip3 install --upgrade pip

RUN pip3 install -r /usr/src/requirements.txt

COPY . /usr/src

WORKDIR /usr/src

CMD celery --app celery_app.worker.celery worker --loglevel=info