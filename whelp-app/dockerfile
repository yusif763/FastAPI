FROM python:3.8

WORKDIR /usr/src

COPY . .

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:8000 main:app --preload -w 4 -k uvicorn.workers.UvicornWorker --access-logfile - --error-logfile - --log-level info