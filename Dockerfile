FROM python:3.8

ENV FLASK_APP=TP
ADD . www/app/

WORKDIR /www/app

RUN pip install pipenv
RUN pipenv install

# TO FIX : ModuleNotFoundError: No module named 'flask'
CMD python ./src/main.py