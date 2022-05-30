FROM python:3 

WORKDIR /b2b_api
COPY . .

ENV FLASK_DEBUG 0
ENV FLASK_ENV production
ENV FLASK_APP main.py

ENV DB_HOST "cluster-b2b-01.cluster-ro-c6tid4wxmmxn.us-east-1.rds.amazonaws.com"
ENV DB_PORT "3306"
ENV DB_NAME "b2b-data"
ENV DB_USER "cademsmart"
ENV DB_PASS "Cadem2018"


RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python3","./main.py"]
