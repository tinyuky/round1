FROM python:3.8

EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ADD requirements.txt .
RUN python -m pip install -r requirements.txt
RUN pip install -U flask-cors

WORKDIR /app
ADD . /app