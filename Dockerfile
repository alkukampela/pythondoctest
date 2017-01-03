FROM python:alpine

RUN mkdir /code

ADD . /code

WORKDIR /code

# Installing sanic needs these
RUN apk add --no-cache --virtual .sanic-deps \
    g++ \
 	make \
    && pip3 install -r requirements.txt \
    && apk del .sanic-deps

CMD ["python", "app.py"]