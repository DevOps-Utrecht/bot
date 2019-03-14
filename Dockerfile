FROM python:3.7
MAINTAINER DevOps

COPY . /bot
WORKDIR /bot
RUN pipenv sync

CMD ["pipenv", "run", "start"]
