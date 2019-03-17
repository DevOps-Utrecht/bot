FROM python:3.6
LABEL maintainer "DevOps http://devops-utrecht.nl"

COPY . /bot
WORKDIR /bot
RUN pip3 install --no-cache-dir -U pip pipenv \
    && pipenv install --system --deploy

CMD ["pipenv", "run", "start"]
