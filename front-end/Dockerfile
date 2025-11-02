# https://uprogramisty.pl/dockerfile-wszystko-o-budowaniu-wlasnych-obrazow/#Wstep
# https://hub.docker.com/_/python

FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV FLASK_APP=app.py
    APP_HOST=0.0.0.0
    APP_PORT=8000
    PYTHONUNBUFFERED=1

CMD [ "python", "app.py" ]
