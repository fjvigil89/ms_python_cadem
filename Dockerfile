FROM tiangolo/uwsgi-nginx-flask:python3.9
RUN apk --update add bash nano

COPY . .
ENV FLASK_DEBUG 0
ENV FLASK_ENV production
ENV FLASK_APP main.py

RUN pip install -r requirements.txt