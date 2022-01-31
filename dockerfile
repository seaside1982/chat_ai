# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /chat_ai

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV PYTHONPATH /chat_ai/src

CMD [ "python3", "src/server/server.py"]