FROM python:3.10-slim

ENV MUSL_LOCPATH=en_US.utf8 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    S6_OVERLAY_VERSION=v1.21.4.0 \
    S6_BEHAVIOUR_IF_STAGE2_FAILS=2

RUN apt-get update && apt-get install -y --no-install-recommends \
      curl  > /dev/null && \
    curl -sSL https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz \
    | tar xfz - -C / && \
    apt-get remove curl -y > /dev/null && \
    pip install --upgrade pipenv > /dev/null

RUN apt update -y > /dev/null && \
    apt install -y build-essential libpq-dev

RUN pip install psycopg2-binary --no-binary psycopg2-binary

ADD Pipfile* /opt/app/
WORKDIR /opt/app/
RUN PIP_IGNORE_INSTALLED=1 \
    pipenv install --system --deploy --ignore-pipfile > /dev/null

ADD . /opt/app