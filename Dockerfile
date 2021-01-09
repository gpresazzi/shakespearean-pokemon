FROM python:3.8-alpine

COPY ./poke_restapi /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN python setup.py install

CMD pokemon_server