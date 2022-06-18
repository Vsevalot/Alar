FROM python:3.10-slim

ENV MUSL_LOCPATH=en_US.utf8 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

RUN apt update -y > /dev/null && \
    apt install -y build-essential libpq-dev && \
    apt install postgresql postgresql-contrib -y > /dev/null

RUN pip install psycopg2-binary --no-binary psycopg2-binary && \
    pip install --upgrade pipenv > /dev/null

ADD Pipfile* /opt/app/
WORKDIR /opt/app/
RUN PIP_IGNORE_INSTALLED=1 \
    pipenv install --system --deploy --ignore-pipfile > /dev/null

ADD . /opt/app