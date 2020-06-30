FROM python:3.7-alpine

ADD . /code

WORKDIR /code

CMD ["python", "main.py"]