FROM python:3.6
LABEL maintainer "DevOps http://devops-utrecht.nl"

COPY . /bot
WORKDIR /bot
RUN pip install --no-cache-dir -U pip==19.0.3 pipenv==2018.11.26 \
    && pipenv install --system --deploy

CMD ["pipenv", "run", "start"]
