FROM tiangolo/uwsgi-nginx-flask:python3.11
WORKDIR /app

COPY ./app/requirements.txt /app/
RUN pip install  -r /app/requirements.txt
COPY ./app /app
