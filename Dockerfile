FROM python

RUN mkdir sanic

WORKDIR /sanic

COPY /app /

WORKDIR /sanic/app

RUN pip install sanic sanic_cors mongoengine redis



