FROM python:3.8

ENV FLASK_APP=src/main:app

ADD . www/app/

WORKDIR /www/app

RUN pip3 install pipenv
RUN pipenv install

CMD pipenv run flask run