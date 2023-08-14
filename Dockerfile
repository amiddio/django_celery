FROM python:3.10-alpine3.16

COPY project /project
WORKDIR /project
EXPOSE 8000

RUN pip install -r requirements.txt

RUN adduser --disabled-password project-user

USER project-user
