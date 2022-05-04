FROM python:3.8

ENV FLASK_APP=src/main:app

COPY . /app
WORKDIR /app/src

RUN pip3 install pipenv
RUN pipenv install

CMD pipenv run python main.py